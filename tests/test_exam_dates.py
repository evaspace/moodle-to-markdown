import json
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'tools'))
import exam_dates as ed  # noqa: E402

ICS = """BEGIN:VCALENDAR\r
BEGIN:VEVENT\r
SUMMARY:Analyse : primitives\\, intégrales et suites (EVAL)\r
DESCRIPTION:Matière: Analyse : primitives\\, intégrales et suites\\nType: Examen\r
DTSTART:20261214T070000Z\r
DTEND:20261218T170000Z\r
END:VEVENT\r
BEGIN:VEVENT\r
SUMMARY:Test à distance APIS\r
DTSTART;VALUE=DATE:20261207\r
DTEND;VALUE=DATE:20261208\r
END:VEVENT\r
BEGIN:VEVENT\r
SUMMARY:Cours magistral\r
DTSTART:20261210T080000\r
END:VEVENT\r
BEGIN:VEVENT\r
SUMMARY:Dénombrement et probabilités (EVAL)\r
 \r
DTSTART:20250101T080000\r
END:VEVENT\r
END:VCALENDAR\r
"""


class ExamDates(unittest.TestCase):
    def setUp(self):
        self.syllabus = json.loads(ed.SYLLABUS.read_text(encoding='utf-8'))

    def test_parse_and_filter(self):
        evs = ed.candidates(ed.parse_ics(ICS), 'Auriga', self.syllabus, date(2026, 9, 1))
        self.assertEqual(len(evs), 2)  # course and old event left out
        apis = evs[0]
        self.assertEqual((apis['debut'], apis['fin'], apis['type']), ('2026-12-14', '2026-12-18', 'Examen'))
        self.assertEqual(apis['titre'], 'Analyse : primitives, intégrales et suites')
        self.assertEqual(apis['ecue'], 'maths/S1/APIS')
        self.assertEqual((evs[1]['debut'], evs[1]['type']), ('2026-12-07', 'Test à distance'))
        self.assertNotIn('fin', evs[1])  # all-day DTEND is exclusive

    def test_merge_skips_known_dates(self):
        evs = ed.candidates(ed.parse_ics(ICS), 'Auriga', self.syllabus, date(2026, 9, 1))
        new = ed.merge([{'debut': '2026-12-14', 'fin': '2026-12-18', 'titre': 'Analyse : primitives, intégrales et suites',
                         'type': 'Examen', 'source': 'Auriga'}], evs)
        self.assertNotIn('2026-12-14', [n['debut'] for n in new])  # already in syllabus.json
        self.assertEqual(ed.merge([], evs + evs), sorted(evs, key=lambda e: e['debut']))  # sorted by date
        known = [{'debut': '2026-12-07', 'titre': 'Autre titre', 'type': 'Test à distance'}]
        self.assertNotIn('2026-12-07', [n['debut'] for n in ed.merge(known, evs)])  # same day, same type


    def test_moodle_open_close_pairs_and_course_codes(self):
        ics = ('BEGIN:VCALENDAR\r\n'
               'BEGIN:VEVENT\r\nSUMMARY:MATHS APIS : TEST 1 FR 16 novembre s’ouvre\r\nCATEGORIES:S1-MATHS-2031\r\nDTSTART:20261116T060000Z\r\nEND:VEVENT\r\n'
               'BEGIN:VEVENT\r\nSUMMARY:MATHS APIS : TEST 1 FR 16 novembre se termine\r\nCATEGORIES:S1-MATHS-2031\r\nDTSTART:20261116T120000Z\r\nEND:VEVENT\r\n'
               'BEGIN:VEVENT\r\nSUMMARY:QCM2 s’ouvre\r\nCATEGORIES:2627_I_INF_FISE_S01_CN_PC_MECA_1\r\nDTSTART:20261123T230000Z\r\nEND:VEVENT\r\n'
               'BEGIN:VEVENT\r\nSUMMARY:QCM2 se termine\r\nCATEGORIES:2627_I_INF_FISE_S01_CN_PC_MECA_1\r\nDTSTART:20261124T225900Z\r\nEND:VEVENT\r\n'
               'END:VCALENDAR\r\n')
        evs = ed.candidates(ed.parse_ics(ics), 'Moodle', self.syllabus, date(2026, 9, 1))
        self.assertEqual([(e['titre'], e['debut'], e.get('fin'), e['ecue']) for e in evs], [
            ('MATHS APIS : TEST 1 FR 16 novembre', '2026-11-16', None, 'maths/S1/APIS'),
            ('QCM2', '2026-11-24', None, 'physique/S1/Mécanique')])  # 00:00-23:59 Paris time: one day


    def test_mail_event(self):
        sent = date(2026, 10, 19)
        ev = ed.mail_event('[EPITA]  Ouverture le\xa0lundi 5 octobre 2026, 07:00 : Test 1  FR : ECUE DP', '', date(2026, 10, 3))
        self.assertEqual((ev['summary'], ev['start']), ('Test 1 FR : ECUE DP', date(2026, 10, 5)))
        body = ('Annonces -> X par Maxime Richard, lundi 19 octobre 2026, 12:51 ' + '-' * 30 +
                ' Bonjour à tous, Ci-joint le PLANNING pour les EXAMENS DU B1 qui auront lieu LA SEMAINE DU 26/10. Merci.')
        ev = ed.mail_event('[EPITA]  Scolarité Prépa Lyon : [EXAMENS B1 _ 2627]', body, sent)
        self.assertEqual((ev['start'], ev['end'], ev['categories']), (date(2026, 10, 26), date(2026, 10, 30), 'Scolarité Prépa Lyon'))
        ev = ed.mail_event('[EPITA]  S1-MATHS-2031 : TEST 1 lundi 5 octobre', 'rien', date(2026, 9, 28))
        self.assertEqual(ev['start'], date(2026, 10, 5))
        self.assertIsNone(ed.mail_event('[EPITA]  Cours : Partiel physique', 'par X, lundi 19 octobre 2026 ' + '-' * 30 + ' Les notions à revoir.', sent))
        self.assertIsNone(ed.mail_event('[QCM_SUP_15.09.26]', 'Veuillez trouver vos notes sur 20 du QCM du 15/09/2026', date(2026, 9, 15)))
        self.assertIsNone(ed.mail_event('RE: [EPITA] Test 1 lundi 5 octobre', '', sent))


if __name__ == '__main__':
    unittest.main()

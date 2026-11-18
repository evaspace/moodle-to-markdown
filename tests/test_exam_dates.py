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
        new = ed.merge(self.syllabus['calendrier'], evs)
        self.assertNotIn('2026-12-14', [n['debut'] for n in new])  # already in syllabus.json
        self.assertEqual(ed.merge([], evs + evs), evs)
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


if __name__ == '__main__':
    unittest.main()

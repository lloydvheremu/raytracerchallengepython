import os
import unittest

from src.colors import Color
from src.canvas import Canvas

class TestCanvas(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(5, 3)

    def tearDown(self) -> None:
        os.remove('untitled.ppm')
        

    def test_creating_canvas(self):
        self.assertEqual(self.canvas.width, 5)
        self.assertEqual(self.canvas.height, 3)
        for row in self.canvas.grid:
            self.assertEqual(row, [Color(0,0,0)] * self.canvas.width)
        

    def test_constructed_ppm_header(self):
        ppm_file = self.canvas.ppm
        with open(ppm_file, 'r') as t:
            self.assertEqual(
                "".join(t.readlines()), 
                f"P3\n{self.canvas.width} {self.canvas.height}\n{255}\n"
            ) 

    
    def test_constructed_pixel_data(self):
        ppm_file = self.canvas.ppm
        self.canvas.write_pixel(0, 0, Color(1.5, 0, 0))
        self.canvas.write_pixel(2, 1, Color(0, 0.5, 0))
        self.canvas.write_pixel(4, 2, Color(-0.5, 0, 1))
        self.canvas.construct_pixel_data()
        expected_data = "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 128 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"

        with open(ppm_file, 'r') as t:
            # Combine file contents to one string and remove all `\n` characters
            file_contents  = "".join(t.readlines()[3:]).replace("\n", "").strip()
            self.assertEqual(
                file_contents, 
                expected_data, f'file contents len=>\n{file_contents}\n ==>\n{expected_data}'
            ) 
            
    def test_ppm_file_line_character_count_less_than_70(self):
        ppm_file = self.canvas.ppm
        self.canvas.change_background(Color(1, 0.8, 0.6))
        self.canvas.construct_pixel_data()
        with open(ppm_file, 'r') as t:
            # Combine file contents to one string and remove all `\n` characters
            file_contents  = t.readlines()            
            for line in file_contents:
                self.assertLessEqual(len(line), 70)
        

    def test_ppm_last_line_ends_with_newline_character(self):
        ppm_file = self.canvas.ppm
        self.canvas.change_background(Color(1, 0.8, 0.6))
        self.canvas.construct_pixel_data()
        with open(ppm_file, 'r') as t:
            # Combine file contents to one string and remove all `\n` characters
            last_line_char  = t.readlines()[-1].split(' ')[-1]
            self.assertIn('\n', last_line_char, f' ->>>{last_line_char}')
        
if __name__ == '__main__':
    unittest.main()
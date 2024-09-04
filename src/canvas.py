from src.colors import Color


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = Color(0, 0, 0)
        self.ppm = 'untitled.ppm'
        self.grid = [[self.color] * self.width for pixel in range(self.height)]
        self.ppm_header = f"P3\n{self.width} {self.height}\n255\n"
        self.ppm_content = self.grid.__str__()

        self.__canvas_to_ppm_header()

    def write_pixel(self, x, y, color: Color):
        self.grid[y][x] = color                

    def change_background(self, color: Color):
        self.grid = [[self.color] * self.width for pixel in range(self.height)]

    def get_pixel(self, x, y):
        # Convert colors from decimal to 0-255
        return self.grid[x][y]      

    def __canvas_to_ppm_header(self):
        try:    
            with open(self.ppm, mode='x') as f:
                f.write(self.ppm_header)
        except FileExistsError:
            print('File Exists Dummy')
        

    def construct_pixel_data(self) -> None:
        with open(self.ppm, mode='a') as f:
            color_count = 0
            for row in self.grid:
                for pixel in row:
                    color_count +=1                
                    rgb_value = pixel.to_rgb()
                    r, g, b = rgb_value
                    if color_count < 22:
                        # if color_count == 21: # last item in the row
                        #     f.write(f'{r} {g} {b}')
                        #     color_count +=1
                        # else:
                        f.write(f'{r} {g} {b} ')
                        color_count +=1
                    else:
                        f.write(f'\n{r} {g} {b} ')
                        color_count = 0
            f.write('\n')      

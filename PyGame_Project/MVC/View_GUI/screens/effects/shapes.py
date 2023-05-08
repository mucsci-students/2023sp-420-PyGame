import math
from dataclasses import dataclass

import pygame


@dataclass
class Shape:
    nothing: int


@dataclass
class Rectangle(Shape):
    def __init__(self, x, y, w, h, font_color, text):
        self.shape = pygame.Rect((x, y), (w, h))
        font_size = int(h * 0.75)
        self.font = pygame.font.SysFont(None, font_size)
        self.font_surface = self.font.render(text, True, font_color)
        self.font_rect = self.font_surface.get_rect()
        self.grad_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        self.text = text

    def draw(self, display, color):
        pygame.draw.rect(display, color, self.shape, 2)
        self.font_rect.center = self.shape.center
        self.grad_surface.fill((0, 0, 0, 180))
        display.blit(self.grad_surface, (self.shape.x, self.shape.y))
        display.blit(self.font_surface, self.font_rect)

    def change_colors(self, display, font_color, rect_color, text):
        self.font_surface = self.font.render(text, True, font_color)
        self.draw(display, rect_color)

    def is_hover(self):
        return self.shape.collidepoint(pygame.mouse.get_pos())
    

@dataclass
class Hexagon(Shape):

    def __init__(self, x, y, w, h, text):
        self.text = text
        self.hex_points = []
        self.font_size = int(h * 0.705)
        self.center = (x, y)
        for angle in range(0, 360, 60):
            radians = math.radians(angle)
            px = x + w * math.cos(radians)
            py = y + h * math.sin(radians)
            self.hex_points.append((px, py))

    def draw(self, display, color, font_color, hover_color, border_thickness=0):
        if self.is_hover():
            pygame.draw.polygon(display, hover_color, self.hex_points, border_thickness)
        else:
            pygame.draw.polygon(display, color, self.hex_points, border_thickness)
        font = pygame.font.SysFont(None, self.font_size)
        text_surface = font.render(self.text, True, font_color)
        text_rect = text_surface.get_rect(center=self.center)
        display.blit(text_surface, text_rect)

    def is_hover(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        num_points = len(self.hex_points)
        inside_hex = False
        start_x_pos, start_y_pos = self.hex_points[0]
        for i in range(num_points + 1):
            end_x_pos, end_y_pos = self.hex_points[i % num_points]
            if mouse_y > min(start_y_pos, end_y_pos):
                if mouse_y <= max(start_y_pos, end_y_pos):
                    if mouse_x <= max(start_x_pos, end_x_pos):
                        if start_y_pos != end_y_pos:
                            x_intercept = (mouse_y - start_y_pos) * (end_x_pos - start_x_pos) / (
                                        end_y_pos - start_y_pos) + start_x_pos
                            if start_x_pos == end_x_pos or mouse_x <= x_intercept:
                                inside_hex = not inside_hex
            start_x_pos, start_y_pos = end_x_pos, end_y_pos
        return inside_hex

    def get_button_text(self):
        if self.is_hover():
            return self.text

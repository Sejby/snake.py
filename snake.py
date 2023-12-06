import pygame

class Snake:
    
    def vytvor_okno(SCREEN_WIDTH: int, SCREEN_HEIGHT: int) -> None:
        okno = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Sejby")
        vykresli_pozadi(okno)

    def vykresli_pozadi(okno) -> None:
        pozadi = pygame.Surface(okno.get_size())
        pozadi = pozadi.convert()
        pozadi.fill((77,77,77))

    def nastav_font() -> None:
        font = pygame.font.SysFont("Roboto", 32)
        vygeneruj_pismo(font)

    def vygeneruj_pismo(font) -> None:
        text = font.render('Snake by Šejby',True,(0,0,0))
        text_wrapper = text.get_rect()
    text_wrapper_centerx = 


    def main():
        pygame.init()
        vytvor_okno(SCREEN_WIDTH=800, SCREEN_HEIGHT=600)




if __name__ == "__main__":
    main()
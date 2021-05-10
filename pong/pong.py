from pygame import*

window = display.set_mode((600, 600))
window.fill((160, 160, 160))



clock = time.Clock()


FPS = 60
game = True




while game:
    for events in event.get():
        if events.type == QUIT:
            game = False
    
    
    
    
    
    display.update()
    clock.tick(FPS)        
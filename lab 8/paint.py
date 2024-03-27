# import pygame

# white = (255, 255, 255)
# eraser = (0, 0, 0)
# green = (34, 139, 34)
# blue = (0, 0, 255)
# red = (255, 0, 0)
# yellow = (255, 255, 0)


# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((800, 800))
#     pygame.display.set_caption("Paint")
#     clock = pygame.time.Clock()

#     radius = 15
#     mode = white
#     last_pos = None

#     while True:
#         # handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     return

#                 # determine if a letter key was pressed
#                 if event.key == pygame.K_r:
#                     mode = red
#                 elif event.key == pygame.K_g:
#                     mode = green
#                 elif event.key == pygame.K_b:
#                     mode = blue
#                 elif event.key == pygame.K_y:
#                     mode = yellow
#                 elif event.key == pygame.K_BACKSPACE:
#                     mode = eraser
#                 elif event.key == pygame.K_w:
#                     drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
#                 elif event.key == pygame.K_c:
#                     drawCircle(screen, pygame.mouse.get_pos(), mode)

#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 # start a new line
#                 last_pos = pygame.mouse.get_pos()

#             if event.type == pygame.MOUSEMOTION and event.buttons[0]:
#                 # draw a line from the last point to the current point
#                 if last_pos is not None:
#                     start_pos = last_pos
#                     end_pos = pygame.mouse.get_pos()
#                     drawLineBetween(screen, start_pos, end_pos, radius, mode)
#                     last_pos = end_pos

#         pygame.display.flip()
#         clock.tick(60)


# def drawLineBetween(screen, start, end, width, color_mode):
#     c1 = max(0, min(255, 2 * start[0] - 256))
#     c2 = max(0, min(255, 2 * start[1]))

#     color = color_mode
#     dx = start[0] - end[0]
#     dy = start[1] - end[1]
#     iterations = max(abs(dx), abs(dy))

#     for i in range(iterations):
#         progress = 1.0 * i / iterations
#         aprogress = 1 - progress
#         x = int(aprogress * start[0] + progress * end[0])
#         y = int(aprogress * start[1] + progress * end[1])
#         pygame.draw.circle(screen, color, (x, y), width)


# def drawRectangle(screen, mouse_pos, w, h, color):
#     x = mouse_pos[0]
#     y = mouse_pos[1]
#     rect = pygame.Rect(x, y, w, h)
#     pygame.draw.rect(screen, color, rect, 3)  # 4th parameter is outline of the rectangle


# def drawCircle(screen, mouse_pos, color):
#     x = mouse_pos[0]
#     y = mouse_pos[1]
#     pygame.draw.circle(screen, color, (x, y), 100, 3)  # 4th parameter is outline of the rectangle


# main()

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
RED = 1
YELLOW = -1
EMPTY = 0
show = {EMPTY:"⚪️", RED: "🔴", YELLOW: "🟡"}
pieces = {EMPTY: "", RED: "red", YELLOW: "yellow"}
simple = {EMPTY: ".", RED: "R", YELLOW: "Y"}
cols = "ABCDEFG"

class Board:

    def __init__(self):
        self.cells = [[0 for _ in range(7)] for _ in range(6)]
        self.player = RED
        self.winner = EMPTY
        self.draw = False
        self.forfeit = False
        self.latest_x, self.latest_y = -1, -1

    def __repr__(self):
        result = ""
        for y in range(6):
            for x in range(7):
                result += show[self.cells[5-y][x]]
            result += "\n"
        result += "\n" + self.message()
        return result

    def message(self):
        if self.winner and self.forfeit:
            return f"{show[self.winner]} wins after an illegal move by {show[-1*self.winner]}\n"
        elif self.winner:
            return f"{show[self.winner]} wins\n"
        elif self.draw:
            return "The game is a draw\n"
        else:
            return f"{show[self.player]} to play\n"
        
    def html(self):
        result = '<div style="text-align: center;font-size:24px">'
        result += self.__repr__().replace("\n","<br/>")
        result += '</div>'
        return result

    def svg(self):
        """Convert the board state to an SVG representation"""
        svg = '''
        <div style="display: flex; justify-content: center;">
        <svg width="450" height="420" viewBox="0 0 450 420">
            <!-- Definitions for gradients and clips -->
            <defs>
                <radialGradient id="redGradient" cx="0.5" cy="0.3" r="0.7">
                    <stop offset="0%" stop-color="#ff6666"/>
                    <stop offset="100%" stop-color="#cc0000"/>
                </radialGradient>
                <radialGradient id="yellowGradient" cx="0.5" cy="0.3" r="0.7">
                    <stop offset="0%" stop-color="#ffff88"/>
                    <stop offset="100%" stop-color="#cccc00"/>
                </radialGradient>
                <linearGradient id="emptyGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#ffffff"/>
                    <stop offset="100%" stop-color="#e0e0e0"/>
                </linearGradient>
    
                <!-- Define the mask for the holes -->
                <mask id="holes">
                    <rect x="25" y="25" width="400" height="320" fill="white"/>
                    '''
        # Add the holes to the mask
        svg += ''.join(f'''
                    <circle 
                        cx="{(x * 50) + 75}" 
                        cy="{(y * 50) + 60}" 
                        r="20" 
                        fill="black"
                    />
                    '''
                    for y in range(6)
                    for x, cell in enumerate(self.cells[5-y])
                )
        
        svg += '''
                </mask>
            </defs>

            <!-- Stand -->
            <path d="M0 360 L25 300 H425 L450 360 L425 385 H25 Z" fill="#004fa3"/>
            
            <!-- Game pieces (will show through the holes) -->
            '''
        
        # Add pieces
        svg += ''.join(f'''
                <circle 
                    class="{f'new-piece' if x == self.latest_x and y == (5-self.latest_y) else ''}"
                    cx="{(x * 50) + 75}"
                    cy="{(y * 50) + 60}"
                    r="20" 
                    fill="{
                        'url(#redGradient)' if (cell == RED) else 
                        'url(#yellowGradient)' if (cell == YELLOW) else 
                        'none'
                    }"
                    stroke="{
                        '#cc0000' if (cell == RED) else
                        '#cccc00' if (cell == YELLOW) else
                        'none'
                    }"
                    stroke-width="1"
                />
                <circle 
                    class="{f'new-piece-highlight' if x == self.latest_x and y == (5-self.latest_y) else ''}"
                    cx="{(x * 50) + 75 - 5}"
                    cy="{(y * 50) + 60 - 5}"
                    r="8" 
                    fill="{
                        '#ff8888' if (cell == RED) else
                        '#ffff99' if (cell == YELLOW) else
                        'none'
                    }"
                    opacity="0.3"
                />
                '''
                for y in range(6)
                for x, cell in enumerate(self.cells[5-y])
                if cell != EMPTY
            )

        svg += '''

            <!-- Board overlay with holes -->
            <rect x="25" y="25" width="400" height="320" fill="#0066cc" rx="10" mask="url(#holes)"/>
            
            <!-- Hole borders (on top of everything for better 3D effect) -->
            '''
        
        # Add hole borders on top
        svg += ''.join(f'''
                <circle 
                    cx="{(x * 50) + 75}" 
                    cy="{(y * 50) + 60}" 
                    r="20" 
                    fill="none"
                    stroke="#005ab3"
                    stroke-width="2"
                />
                '''
                for y in range(6)
                for x, cell in enumerate(self.cells[5-y])
            )
        
        svg += '''
        </svg>
    </div>
    <style>
        .new-piece {
            animation: dropPiece 0.5s cubic-bezier(0.95, 0.05, 1, 0.5);
        }
        .new-piece-highlight {
            animation: dropPiece 0.5s cubic-bezier(0.95, 0.05, 1, 0.5);
        }
        @keyframes dropPiece {
            from {
                transform: translateY(-300px);
            }
            to {
                transform: translateY(0);
            }
        }
    </style>
    '''
        return svg

    def json(self):
        result = "{\n"
        result += '    "Column names": ["A", "B", "C", "D", "E", "F", "G"],\n'
        for y in range(6):
            result += f'    "Row {6-y}": [' 
            for x in range(7):
                result += f'"{pieces[self.cells[5-y][x]]}", '
            result = result[:-2] + '],\n'
        result = result[:-2]+'\n}'
        return result

    def alternative(self):
        result = "ABCDEFG\n"
        for y in range(6):
            for x in range(7):
                result += simple[self.cells[5-y][x]]
            result += "\n"
        return result

    def height(self, x):
        height = 0
        while height<6 and self.cells[height][x] != EMPTY:
            height += 1
        return height

    def legal_moves(self):
        return [cols[x] for x in range(7) if self.height(x)<6]

    def illegal_moves(self):
        return [cols[x] for x in range(7) if self.height(x)==6]

    def winning_line(self, x, y, dx, dy):
        color = self.cells[y][x]
        for pointer in range(1, 4):
            xp = x + dx * pointer
            yp = y + dy * pointer
            if not (0 <= xp <= 6 and 0 <= yp <= 5) or self.cells[yp][xp] != color:
                return EMPTY
        return color
    
    def winning_cell(self, x, y):
        for dx, dy in ((0, 1), (1, 1), (1, 0), (1, -1)):
            if winner := self.winning_line(x, y, dx, dy):
                return winner
        return EMPTY
    
    def wins(self):
        for y in range(6):
            for x in range(7):
                if winner := self.winning_cell(x, y):
                    return winner
        return EMPTY
    
    def move(self, x):
        y = self.height(x)
        self.cells[y][x] = self.player
        self.latest_x, self.latest_y = x, y
        if winner := self.wins():
            self.winner = winner
        elif not self.legal_moves:
            self.draw = True
        else:
            self.player = -1 * self.player
        return self

    def is_active(self):
        return not self.winner and not self.draw
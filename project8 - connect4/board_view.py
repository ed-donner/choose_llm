RED = 1
YELLOW = -1
EMPTY = 0

def to_svg(board):
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
                for x, cell in enumerate(board.cells[5-y])
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
                class="{f'new-piece' if x == board.latest_x and y == (5-board.latest_y) else ''}"
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
                class="{f'new-piece-highlight' if x == board.latest_x and y == (5-board.latest_y) else ''}"
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
            for x, cell in enumerate(board.cells[5-y])
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
            for x, cell in enumerate(board.cells[5-y])
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
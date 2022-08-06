import bitboards as bb

class BitChess:

    def __init__(self, board=None):
        BitChess.setup(self, board)

    def __repr__(self):
        return BitChess.repboard(self)

    def WhiteLegalPawn(self, pos):
        l = 0
        if pos > 36028797018963968:
            pass
        if pos << 8 & self.location == 0:
            l = l | pos << 8
            if pos < 65536:
                if pos << 16 & self.location == 0:
                    l = l | pos << 16
        if pos & self.coloumn[0]:
            if pos << 9 & self.black_location > 0:
                l = l | pos << 9
        elif pos & self.coloumn[7]:
            if pos << 7 & self.black_location > 0:
                l = l | pos << 7
        else:
            if pos << 9 & self.black_location > 0:
                l = l | pos << 9
            if pos << 7 & self.black_location > 0:
                l = l | pos << 7
        return l

    def WhiteLegalRook(self, pos):
        legal = 0
        for i, l in enumerate(self.rank):
            if l & pos != 0:
                r = i
                break
        for i, l in enumerate(self.coloumn):
            if l & pos != 0:
                c = i
                break
        dl, dr = 7-c, c
        dt, db = 7-r, r
        for i in range(dl):
            t = i+1
            if pos << t & self.white_location != 0:
                break
            legal = legal | pos << t
            if pos << t & self.black_location != 0:
                break
        for i in range(dr):
            t = i+1
            if pos >> t & self.white_location != 0:
                break
            legal = legal | pos >> t
            if pos >> t & self.black_location != 0:
                break
        for i in range(dt):
            t = 8*(i+1)
            if pos << t & self.white_location != 0:
                break
            legal = legal | pos << t
            if pos << t & self.black_location != 0:
                break
        for i in range(db):
            t = 8*(i+1)
            if pos >> t & self.white_location != 0:
                break
            legal = legal | pos >> t
            if pos >> t & self.black_location != 0:
                break
        return legal

    def WhiteLegalBishop(self, pos):
        legal = 0
        for i, l in enumerate(self.rank):
            if l & pos != 0:
                r = i
                break
        for i, l in enumerate(self.coloumn):
            if l & pos != 0:
                c = i
                break
        dl, dr = c, 7-c
        dt, db = 7-r, r
        tl = min(dl, dt)
        tr = min(dr, dt)
        bl = min(dl, db)
        br = min(dr, db)
        for i in range(tr):
            t = 9*(i+1)
            if pos << t & self.white_location != 0:
                break
            legal += pos << t
            if pos << t & self.black_location != 0:
                break
        for i in range(bl):
            t = 9*(i+1)
            if pos >> t & self.white_location != 0:
                break
            legal += pos >> t
            if pos >> t & self.black_location != 0:
                break
        for i in range(br):
            t = 7*(i+1)
            if pos << t & self.white_location != 0:
                break
            legal += pos << t
            if pos << t & self.black_location != 0:
                break
        for i in range(tl):
            t = 7*(i+1)
            if pos >> t & self.white_location != 0:
                break
            legal += pos >> t
            print(pos, legal)
            if pos >> t & self.black_location != 0:
                break
        return legal

    def WhiteLegalQueen(self, pos):
        return BitChess.WhiteLegalRook(self, pos) + BitChess.WhiteLegalBishop(self, pos)

    def WhiteLegalKnight(self, pos):
        pos = len(bin(pos))-3
        m = self.knight[pos] ^ self.white_location
        l = m & self.knight[pos]
        return l

    def WhiteLegalKing(self, pos):
        pos = len(bin(pos))-3
        m = self.king[pos] ^ self.white_location
        l = m & self.king[pos]
        return l

    def BlackLegalPawn(self, pos):
        l = 0
        if pos < 256:
            pass
        if pos >> 8 & self.location == 0:
            l = l | pos >> 8
            if pos > 140737488355328:
                if pos >> 16 & self.location == 0:
                    l = l | pos >> 16
        if pos & self.coloumn[0]:
            if pos >> 7 & self.white_location > 0:
                l = l | pos >> 7
        elif pos & self.coloumn[7]:
            if pos >> 9 & self.white_location > 0:
                l = l | pos >> 9
        else:
            if pos >> 9 & self.white_location > 0:
                l = l | pos >> 9
            if pos >> 7 & self.white_location > 0:
                l = l | pos >> 7
        return l

    def BlackLegalRook(self, pos):
        legal = 0
        for i, l in enumerate(self.rank):
            if l & pos != 0:
                r = i
                break
        for i, l in enumerate(self.coloumn):
            if l & pos != 0:
                c = i
                break
        dl, dr = 7-c, c
        dt, db = 7-r, r
        for i in range(dl):
            t = i+1
            if pos << t & self.black_location != 0:
                break
            legal = legal | pos << t
            if pos << t & self.white_location != 0:
                break
        for i in range(dr):
            t = i+1
            if pos >> t & self.black_location != 0:
                break
            legal += pos >> t
            if pos >> t & self.white_location != 0:
                break
        for i in range(dt):
            t = 8*(i+1)
            if pos << t & self.black_location != 0:
                break
            legal = legal | pos << t
            if pos << t & self.white_location != 0:
                break
        for i in range(db):
            t = 8*(i+1)
            if pos >> t & self.black_location != 0:
                break
            legal = legal | pos >> t
            if pos >> t & self.white_location != 0:
                break
        return legal

    def BlackLegalBishop(self, pos):
        legal = 0
        for i, l in enumerate(self.rank):
            if l & pos != 0:
                r = i
                break
        for i, l in enumerate(self.coloumn):
            if l & pos != 0:
                c = i
                break
        dl, dr = 7-c, c
        dt, db = 7-r, r
        tl = min(dl, dt)
        tr = min(dr, dt)
        bl = min(dl, db)
        br = min(dr, db)
        for i in range(tl):
            t = 9*(i+1)
            if pos << t & self.black_location != 0:
                break
            legal = legal | pos << t
            if pos << t & self.white_location != 0:
                break
        for i in range(bl):
            t = 9*(i+1)
            if pos >> t & self.black_location != 0:
                break
            legal = legal | pos >> t
            if pos >> t & self.white_location != 0:
                break
        for i in range(br):
            t = 7*(i+1)
            if pos << t & self.black_location != 0:
                break
            legal = legal | pos << t
            if pos << t & self.white_location != 0:
                break
        for i in range(tr):
            t = 7*(i+1)
            if pos >> t & self.black_location != 0:
                break
            legal = legal | pos >> t
            if pos >> t & self.white_location != 0:
                break
        return legal

    def BlackLegalQueen(self, pos):
        return BitChess.BlackLegalRook(self, pos) + BitChess.BlackLegalBishop(self, pos)

    def BlackLegalKnight(self, pos):
        pos = len(bin(pos))-3
        m = self.knight[pos] ^ self.black_location
        l = m & self.knight[pos]
        return l

    def BlackLegalKing(self, pos):
        pos = len(bin(pos))-3
        m = self.king[pos] ^ self.black_location
        l = m & self.king[pos]
        return l

    def breakmoves(self, legal):
        l = set([])
        while legal > 0:
            pos = legal&(-legal)
            l.add(pos)
            legal = legal-pos
        return l

    def LegalMoves(self):
        self.white_legal = {}
        self.black_legal = {}
        for k, v in self.white_pieces.items():
            legal = zip(list(map(lambda e: self.white_calc[k](self, e), v)), v)
            for i, j in legal:
                print(k, i)
                self.white_legal[str(j)] = BitChess.breakmoves(self, i)
        for k, v in self.black_pieces.items():
            legal = zip(list(map(lambda e: self.black_calc[k](self, e), v)), v)
            for i, j in legal:
                self.black_legal[self.invnames[str(j)]] = BitChess.breakmoves(self, i)

    def setup(self, board=False):
        self.dark = bb.DARK_SQUARES
        self.light = bb.LIGHT_SQUARES
        self.names = bb.SQUARE_NAMES
        self.invnames = bb.INV_NAMES
        self.rank = bb.RANK
        self.coloumn = bb.COLOUMN
        self.diagbl = bb.DIAGONALSBL
        self.diagtl = bb.DIAGONALSTL
        self.knight = bb.KNIGHTMOVES
        self.king = bb.KINGMOVES
        self.white_calc = {'P':BitChess.WhiteLegalPawn,
                           'R':BitChess.WhiteLegalRook,
                           'N':BitChess.WhiteLegalKnight,
                           'B':BitChess.WhiteLegalBishop,
                           'Q':BitChess.WhiteLegalQueen,
                           'K':BitChess.WhiteLegalKing}
        self.black_calc = {'p':BitChess.BlackLegalPawn,
                           'r':BitChess.BlackLegalRook,
                           'n':BitChess.BlackLegalKnight,
                           'b':BitChess.BlackLegalBishop,
                           'q':BitChess.BlackLegalQueen,
                           'k':BitChess.BlackLegalKing}
        if not board:
            self.white_location = bb.STARTINGWHITE
            self.black_location = bb.STARTINGBLACK
            self.location = bb.STARTINGPOS
            self.white_pieces = bb.WHITELOCATION
            self.black_pieces = bb.BLACKLOCATION
        else:
            BitChess.confen(self, board)
        BitChess.LegalMoves(self)

    def confen(self, fen):
        self.white_location = 0
        self.black_location = 0
        self.white_pieces = {i:set([]) for i in bb.WHITELOCATION}
        self.black_pieces = {i:set([]) for i in bb.BLACKLOCATION}
        values = fen.split()
        board = values[0].split('/')
        for i, v in enumerate(board):
            s = 0
            for j in v:
                if j in self.white_pieces:
                    loc = 2**(8*(7-i)) << s
                    self.white_pieces[j].add(loc)
                    self.white_location += loc
                elif j in self.black_pieces:
                    loc = 2**(8*(7-i)) << s
                    self.black_pieces[j].add(loc)
                    self.black_location += loc
                else:
                    s -= 1
                    s += int(j)
                s += 1
        self.location = self.white_location + self.black_location

    @staticmethod
    def mirrfen(board):
        l = []
        c = 0
        for i in board:
            s = ''
            c = 0
            for v, j in enumerate(i):
                if j != ' ':
                    if c > 0:
                        s += str(c)
                    s += j
                    c = 0
                else:
                    c += 1
                if v == 7 and c > 0:
                    s += str(c)
            if s == '':
                s = '8'
            l.append(s)
        fen = ''
        for i in l:
            fen += i+"/"
        return fen[:-1]


    def genwindow(self):
        board = [[" " for j in range(8)] for i in range(8)]

        for i, v in self.white_pieces.items():
            for j in v:
                j = len(bin(j))-3
                r = j % 8
                d = j // 8
                board[d][7-r] = i

        for i, v in self.black_pieces.items():
            for j in v:
                j = len(bin(j))-3
                r = j % 8
                d = j // 8
                board[d][7-r] = i

        return [[j for j in i[::-1]] for i in board[::-1]]

    def repboard(self):
        board = BitChess.genwindow(self)
        s = ""
        for i in board:
            s += " ---"*8 + "\n"
            for j in i:
                s += f"| {j} "
            s += "|" + "\n"
        s += " ---"*8 + "\n"
        return s

b = [[' ' for i in range(8)] for j in range(8)]
b[3][4] = 'B'
c = BitChess('rnb1k2r/p1p3pp/1p4n1/4R2Q/8/2NB3P/PPPB1PP1/R5K1 b kq - 0 16')
print(c)
print(c.white_legal)

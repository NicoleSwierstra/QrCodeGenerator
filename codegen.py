
alignmentCols = [
        [],                     # 0
        [],                     # 1
        [6, 18],                # 2
        [6, 22],                # 3
        [6, 26],                # 4
        [6, 30],                # 5
        [6, 34],                # 6
        [6, 22, 38],            # 7
        [6, 24, 42],            # 8
        [6, 26, 46],            # 9
        [6, 28, 50],            # 10
        [6, 30, 54],            # 11
        [6, 32, 58],            # 12
        [6, 34, 62],            # 13
        [6, 26, 46, 66],        # 14
        [6, 26, 48, 70],        # 15
        [6, 26, 50, 74],        # 16
        [6, 30, 54, 78],        # 17
        [6, 30, 56, 82],        # 18
        [6, 30, 58, 86],        # 19
        [6, 34, 62, 90],        # 20
    ]


class Code:

    def __init__(this, string, version):
        this.length = len(string)
        
        this.side_length = (((version - 1) * 4) + 21)
        this.bits = [ [0]*this.side_length for i in range(this.side_length)]

        for i in range(0, 5):
            this.bits[i + 1][1] = 1
            this.bits[i + 1][5] = 1
            this.bits[1][i + 1] = 1
            this.bits[5][i + 1] = 1

            this.bits[i + 1][-2] = 1
            this.bits[i + 1][-6] = 1
            this.bits[1][i - 6] = 1
            this.bits[5][i - 6] = 1

            this.bits[i - 6][1] = 1
            this.bits[i - 6][5] = 1
            this.bits[-2][i + 1] = 1
            this.bits[-6][i + 1] = 1

        for i in range(0, 8):
            this.bits[i][7] = 1
            this.bits[7][i] = 1
            
            this.bits[i][-8] = 1
            this.bits[7][-i] = 1
            
            this.bits[-8][i] = 1
            this.bits[-i-1][7] = 1

        for i in range(0, this.side_length - 16):
            this.bits[6][i + 8] = i % 2
            this.bits[i + 8][6] = i % 2

        pattern = [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ]
        
        acols = len(alignmentCols[version])

        for ii in range(acols):
            for jj in range(acols):
                i = alignmentCols[version][ii]
                j = alignmentCols[version][jj]
                

                if (ii == 0 and jj == 0) or (ii == 0 and jj == acols-1) or (ii == acols-1 and jj == 0):
                    continue

                for x in range(-2, 3):
                    for y in range(-2, 3):
                        this.bits[i + y][j + x] = pattern[x + 2][y + 2]

        this.bits[(4 * version) + 9][8] = 0

    def get_pixels(this):
        pass

    def print(this):
        chars = [" ", "▀", "▄", "█"]
        for i in range(0, this.side_length - 1, 2):
            for j in range(0, this.side_length):
                c = this.bits[i + 1][j] * 2 + this.bits[i][j]

                print(chars[c], end="")
            print()

        for i in range(0, this.side_length):
            print(chars[this.bits[-1][i]], end="")

        print()


if __name__ == "__main__":
    for i in range(0, 21, 4):
        print("\n\n\n version " + str(i) + ": ")
        c = Code("h", i)
        c.print()
    

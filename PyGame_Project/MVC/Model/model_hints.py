
class Hints:
    def __init__(self, words, pangram):
        self.words = self.fix_wordList(words)
        self.pangram = pangram
        self.first_letters = self.get_first_letter()
        self.is_bingo = self.get_bazinga()
        self.max_length = self.get_max_length()
        self.two_letter_dict = self.get_first_two_letters()
        self.two_d_array = self.get_2d_array()

    def fix_wordList(self, words):
        ## Converting out List-List to List
        WordList = []
        for word in words:
            WordList.append(word[0])
        return WordList

    def get_first_letter(self):
        first_letters = set(word[0] for word in self.words)
        return first_letters

    def get_first_two_letters(self):
        # Add first two letters of each word to dict
        hint_info = {}
        for word in self.words:
            first_two = word[:2]
            key = first_two
            if key in hint_info:
                hint_info[key] += 1
            else:
                hint_info[key] = 1
        return hint_info

    def get_bazinga(self):
        if set(self.pangram).issubset(self.first_letters):
            return True
        else:
            return False

    def get_max_length(self):
        max_len = 0
        for word in self.words:
            if len(word) > max_len:
                max_len = len(word)
        return max_len

    def get_2d_array(self):
        counts = {}
        for word in self.words:
            length = len(word)
            key = (word[0], length)
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
    
        rows = []
        columns = [" "]

        for size in range(4, self.max_length + 1):
            columns.append(size)
        rows.append(columns)
        column_sum = {}
        for letter in self.pangram:
            columns = []
            counter = 0
            columns.append(letter.upper())
            for size in range(4, self.max_length + 1):
                if (letter, size) in counts:
                    if size in column_sum:
                        column_sum[size] += counts[(letter, size)]
                    else:
                        column_sum[size] = counts[(letter, size)]
                    columns.append(counts[(letter, size)])
                    counter += counts[(letter, size)]
                else:
                    columns.append(" ")
            columns.append(counter)
            rows.append(columns)
        columns = []
        length_sum = 0
        columns.append(" ")
        for item in column_sum:
            length_sum += column_sum[item]
            columns.append(column_sum[item])
        columns.append(length_sum)
        rows.append(columns)
        return rows

# word_list = ['calcicoles', 'socialises', 'callaloos', 'ceaseless', 'classical', 'classless', 'coalesces', 'colessees', 'ecclesiae', 'ecclesial', 'isosceles', 'localises', 'salsillas', 'scaleless', 'scolioses', 'scoliosis', 'secaloses', 'silicoses', 'silicosis', 'socialise', 'solecises', 'accesses', 'asocials', 'assesses', 'calicles', 'calicoes', 'calloses', 'caseases', 'caseoses', 'cassises', 'celosias', 'cicelies', 'classico', 'classics', 'coalesce', 'coalless', 'coeliacs', 'colessee', 'colossal', 'ecclesia', 'ecesises', 'isleless', 'laceless', 'laicises', 'localise', 'loessial', 'lossless', 'ossicles', 'sailless', 'salsilla', 'scissile', 'scoleces', 'scolices', 'secalose', 'silesias', 'silicles', 'soilless', 'solecise', 'soleless', 'acacias', 'alcaics', 'alcools', 'aliases', 'alleles', 'asceses', 'ascesis', 'asocial', 'assails', 'assoils', 'calesas', 'calices', 'calicos', 'callees', 'callose', 'casease', 'caseose', 'cassias', 'celiacs', 'celosia', 'cicalas', 'cilices', 'ciscoes', 'cissies', 'classes', 'classic', 'classis', 'cloacas', 'collies', 'colossi', 'coolies', 'ecloses', 'iceless', 'icicles', 'laicise', 'lassies', 'lassoes', 'lessees', 'liaises', 'locales', 'loessal', 'loesses', 'loessic', 'loiases', 'loiasis', 'lollies', 'ossicle', 'sallies', 'sassies', 'scillas', 'sessile', 'silesia', 'silicas', 'silicic', 'silicle', 'sillies', 'sissies', 'socials', 'solaces', 'aaliis', 'access', 'aiolis', 'aisles', 'allees', 'allies', 'assail', 'assais', 'assess', 'assoil', 'cacaos', 'calces', 'calesa', 'callas', 'caseic', 'cassia', 'cassis', 'ceases', 'ceilis', 'cellos', 'cesses', 'ciscos', 'closes', 'coalas', 'cocoas', 'colics', 'colies', 'cooees', 'cosecs', 'cosies', 'easels', 'easies', 'ecesic', 'ecesis', 'eclose', 'isseis', 'lasses', 'lassie', 'lassis', 'lassos', 'leases', 'lessee', 'liaise', 'liases', 'lilacs', 'lilies', 'lisles', 'locals', 'locies', 'locoes', 'looies', 'looses', 'losels', 'losses', 'ollies', 'saices', 'salals', 'salols', 'salsas', 'sasses', 'scales', 'scalls', 'scilla', 'seccos', 'seises', 'selles', 'sialic', 'silica', 'sisals', 'sisses', 'slices', 'social', 'socles', 'solace', 'soloes', 'acais', 'aisle', 'alecs', 'alias', 'aloes', 'assai', 'asses', 'cacas', 'calls', 'calos', 'casas', 'cases', 'cease', 'ceils', 'cells', 'cisco', 'class', 'close', 'coals', 'cocas', 'cocos', 'coils', 'colas', 'coles', 'cools', 'cosec', 'coses', 'cosie', 'easel', 'eases', 'esses', 'isles', 'issei', 'laces', 'laics', 'lalls', 'lases', 'lassi', 'lasso', 'lease', 'lisle', 'locis', 'locos', 'loess', 'lolls', 'loose', 'losel', 'loses', 'oases', 'oasis', 'oleos', 'olios', 'ollas', 'ossia', 'saice', 'sails', 'salal', 'sales', 'salic', 'salol', 'salsa', 'scale', 'scall', 'seals', 'secco', 'seels', 'seise', 'selle', 'sells', 'sials', 'sices', 'sills', 'silos', 'sisal', 'sises', 'slice', 'sloes', 'socas', 'soces', 'socle', 'soils', 'solas', 'solei', 'soles', 'solos', 'aals', 'aces', 'ails', 'alas', 'ales', 'alls', 'also', 'asci', 'asea', 'casa', 'case', 'cees', 'cels', 'cess', 'cols', 'coos', 'coss', 'ease', 'ecos', 'eels', 'ells', 'else', 'eses', 'esse', 'ices', 'ills', 'isle', 'lacs', 'lase', 'lass', 'leas', 'lees', 'leis', 'less', 'lias', 'lies', 'loos', 'lose', 'loss', 'ocas', 'oils', 'oles', 'oses', 'ossa', 'sacs', 'sail', 'sale', 'sall', 'sals', 'sass', 'seal', 'seas', 'secs', 'seel', 'sees', 'seis', 'sell', 'sels', 'sial', 'sice', 'sics', 'sill', 'silo', 'sloe', 'soca', 'soil', 'sola', 'sole', 'soli', 'solo', 'sols']
# puzzle_letters = 'lisaeco'
# hint = Hints(word_list, puzzle_letters)
# print(hint.two_d_array)

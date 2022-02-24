


from unicodedata import name


class Cave():

    def __init__(self, name: str):
        self.name = name
        self.connections = []

    def update_connections(self, cave_name):
        self.connections.append(cave_name)


class Map():

    def __init__(self, connections):

        self.connections = connections
        self.cave_names = []
        self.caves = []
        
        self.map()

    def map(self):
        self._get_list_of_caves()
        self._create_caves()
        self._create_connections()

    def _get_list_of_caves(self):
        for connection in self.connections:
            for cave in connection.split('-'):
                if cave not in self.cave_names:
                    self.cave_names.append(cave)

    def _create_caves(self):
        for cave_name in self.cave_names:
            self.caves.append(Cave(cave_name))

    def _create_connections(self):
        for connection in connections:
            start, end = connection.split('-')
            start_id = self.cave_names.index(start)
            end_id = self.cave_names.index(end)
            self.caves[start_id].update_connections(end)
            self.caves[end_id].update_connections(start)

    def _find_routes(self):

        paths = [['start']]
        new_paths = []
        for path in paths: #ojo que igual lo tengo que hacer pa atrás
            current_id = self.cave_names.index(path[-1])
            used_small_caves = [cave for cave in path if not cave.isupper()]
            possibilities = self.caves[current_id].connections
            for cave in possibilities:
                if cave not in used_small_caves:
                    new_path = path.copy()
                    new_path.append(cave)
                    new_paths.append(new_path)
        print(new_paths)




archivo = './Inputs/example12.txt'

with open(archivo) as data:
    connections = data.readlines()

connections = [item.rstrip("\n") for item in connections]

a = Map(connections)
a._find_routes()
a._find_routes()

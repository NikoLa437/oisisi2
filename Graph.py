class Graph:
    def __init__(self):
        self._outgoing = {}
        self._incoming = {}

    def add_vertex(self, vertex):

        self._outgoing[vertex] = []
        if vertex not in self._incoming.keys():
            self._incoming[vertex] = []

    def add_edge(self, vertex, vertexToAppend):

        self._outgoing[vertex].append(vertexToAppend)
        if vertexToAppend not in self._incoming.keys():
            self._incoming[vertexToAppend] = []

        self._incoming[vertexToAppend].append(vertex)

    def add_from_html(self, vertex, links):

        self.add_vertex(vertex)
        for link in links:
            self.add_edge(vertex, link)

    def get_incoming(self, vertex):
        return list(self._incoming[vertex])

    def get_outgoing(self, vertex):
        return list(self._outgoing[vertex])

    def vertices(self):
        return list(self._outgoing.keys())
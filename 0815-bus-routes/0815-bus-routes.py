class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        adj_list = defaultdict(list)
        for route, stops in enumerate(routes):
            for stop in stops:
                adj_list[stop].append(route)

        q = deque()
        vis = set()

        for route in adj_list.get(source, []):
            q.append(route)
            vis.add(route)
        bus_count = 1 
        while q:
            size = len(q)
            for i in range(size):
                route = q.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return bus_count
                    for next_route in adj_list.get(stop, []):
                        if next_route not in vis:
                            vis.add(next_route)
                            q.append(next_route)

            bus_count += 1


        return -1

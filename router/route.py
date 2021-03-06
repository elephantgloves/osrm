class RouteObject(object):

    def __init__(self, endpoints, routejson):
        self.text = routejson
        self.endpoints = endpoints

        self.length = routejson[0]["distance"]
        self.traveltime = routejson[0]["duration"]
        self.waypoints = [step["maneuver"]["location"] for step in routejson[0]["legs"][0]["steps"]]

    def parseRoute(self):
        return [self.length, self.traveltime, self.waypoints]

    def totalRouteLength(self):
        return self.length

    def getLegDetails(self):
        pass

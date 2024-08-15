#1 

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_destinations = our_routes.intersection(competitor_routes)

unique_our_destinations = our_routes.difference(competitor_routes)

unique_competitor_destinations = competitor_routes.difference(our_routes)

neither_shared_destinations = unique_our_destinations.union(unique_competitor_destinations)

print(f"Destinations that both airlines fly to: {shared_destinations}")
print(f"Destinations unique to our airline: {unique_our_destinations}")
print(f"Destinations unique to competitor airline: {unique_competitor_destinations}")
print(f"Destinations that neither airline shares: {neither_shared_destinations}")

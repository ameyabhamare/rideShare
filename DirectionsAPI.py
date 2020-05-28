
import herepy
def extract_route(lat1,long1,lat2,long2):
    
    #geocoderApi = herepy.GeocoderApi('dpwPxdRJaF8n59ULKx8R', 'ldLYs1bJmd-MguUYeSiL6w')

    routingApi = herepy.RoutingApi('dpwPxdRJaF8n59ULKx8R', 'ldLYs1bJmd-MguUYeSiL6w')

#response = geocoderApi.free_form('200 S Mathilda Sunnyvale CA')

    response = routingApi.car_route([lat1,long1],[lat2, long2], [herepy.RouteMode.car, herepy.RouteMode.fastest])
    return response
#print(response)


'''
import openrouteservice

coords = (( 12.9349637, 77.5328135),(12.9383326, 77.5334036))

client = openrouteservice.Client(key='5b3ce3597851110001cf6248823b8b376ed847818092dcff2d25c439') # Specify your personal API key
routes = client.directions(coords)

print(routes)
'''

'''
response.response['route'][0]['leg'][0]['maneuver'][6]['position']
'''

def clean_data(data,n):
    data = data.response['route'][0]['leg'][0]['maneuver']
    lat_long = []
    for i in range(len(data)):
        temp_list = []
        temp_list.append(data[i]['position']['latitude'])
        temp_list.append(data[i]['position']['longitude'])
        if data[i]['length']>1000 and n:
            #reiterate and return object and assign to data_temp
            data_temp=extract_route(data[i-1]['position']['latitude'],data[i-1]['position']['longitude'],data[i]['position']['latitude'],data[i]['position']['longitude'])
            temp_list = clean_data(data_temp,n-1)
            
            lat_long.extend(temp_list[1:])
        else:
            #temp_list.append(data[i]['length'])
            lat_long.append(tuple(temp_list))
    return lat_long
 #response = routingApi.car_route([ 12.9641891, 77.5701284],[12.963438, 77.5810289], [herepy.RouteMode.car, herepy.RouteMode.fastest])
def main():
    lat1= 12.912701
    long1= 77.599880
    lat2=12.9507
    long2=77.5848
    data=extract_route(lat1,long1,lat2,long2)
    final=clean_data(data,0)
    print(final)
main()
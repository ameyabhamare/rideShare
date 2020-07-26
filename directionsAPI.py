import herepy
def extract_route(lat1,long1,lat2,long2):
    routingApi = herepy.RoutingApi('dpwPxdRJaF8n59ULKx8R', 'ldLYs1bJmd-MguUYeSiL6w')
    response = routingApi.car_route([lat1,long1],[lat2, long2], [herepy.RouteMode.car, herepy.RouteMode.fastest])
    return response

def clean_data(data,n):
    data = data.response['route'][0]['leg'][0]['maneuver']
    lat_long = []
    for i in range(len(data)):
        temp_list = []
        temp_list.append(data[i]['position']['latitude'])
        temp_list.append(data[i]['position']['longitude'])
        if data[i]['length']>1000 and n:
            # re-iterate and return object and assign to data_temp
            data_temp=extract_route(data[i-1]['position']['latitude'],data[i-1]['position']['longitude'],data[i]['position']['latitude'],data[i]['position']['longitude'])
            temp_list = clean_data(data_temp,n-1)
            
            lat_long.extend(temp_list[1:])
        else:
            #temp_list.append(data[i]['length'])
            lat_long.append(tuple(temp_list))
    return lat_long
 
def main():
    lat1= 12.912701
    long1= 77.599880
    lat2=12.9507
    long2=77.5848
    data=extract_route(lat1,long1,lat2,long2)
    final=clean_data(data,0)
    print(final)
main()

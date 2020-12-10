def invalid_naive_algo(municipalities_map, bounds, nb_district):
    districts = [[] for _ in range(nb_district)]

    current_district_idx = 0

    for i in range(municipalities_map.shape[0]):
        for j in range(municipalities_map.shape[1]):
            if current_district_idx < bounds[0][1] and len(districts[current_district_idx]) >= bounds[0][0]:
                current_district_idx += 1
            elif current_district_idx >= bounds[0][1] and len(districts[current_district_idx]) >= bounds[1][0]:
                current_district_idx += 1
            districts[current_district_idx].append((i, j))

    return districts

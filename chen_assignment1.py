import json
import operator
import yaml

with open('hw.json') as myfile:
    data = myfile.read()
parsed_json = json.loads(data)

ppl_ages_dict = parsed_json["ppl_ages"]
age_buckets_list = parsed_json["buckets"]

max_age = max(ppl_ages_dict.items(), key=operator.itemgetter(1))[1]
max_age += 1

age_buckets_list += [0, max_age]
age_buckets_list.sort()
buckets_counter = len(age_buckets_list)

keystring = "{0} - {1}"
result = {}
for i in range(1, buckets_counter):
    values_list = []
    dictkey = keystring.format(age_buckets_list[i-1], age_buckets_list[i])
    for name in ppl_ages_dict:
        if age_buckets_list[i-1] <= ppl_ages_dict[name] < age_buckets_list[i]:
            values_list.append('' + name)
    result[dictkey] = values_list

with open('result', 'w') as yaml_file:
    yaml.dump(result, yaml_file, default_flow_style=False, allow_unicode=True)
    print("yaml output: ", result)

import ijson
import json

data_path = "llava_v1_5_mix665k.json"
# output_file = "llava_v1_5_mix_tv_vg.json"
output_file = "llava_v1_5_mix_tv.json"
filtered_images = []
with open(data_path,'r') as f:
    for item in ijson.items(f,"item"):
        # if item.get("image","").startswith("textvqa/") or item.get("image","").startswith("vg/"):
        if item.get("image","").startswith("textvqa/"):
            filtered_images.append(item)
            # break

with open(output_file,"w") as f:
    json.dump(filtered_images, f, indent=4)


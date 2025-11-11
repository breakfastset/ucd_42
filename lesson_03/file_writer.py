filename = "blog.txt"
num_flowers = 299

out_file = open(filename, "w")
out_file.write("Today I went to gardens by the bay.\n")
out_file.write(f"I saw {num_flowers} flowers there.\n")
out_file.write("Tomorrow, I shall visit Haw Par Villa.\n")

out_file.close()  # always close the file after use

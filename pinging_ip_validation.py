import re
import subprocess

pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
file = open("ip_list.txt", "w")

while True:
    ip = input("Provide IP address ('exit' to quit): ")

    if ip == "exit":
        break

    if re.match(pattern, ip):
        print(f"{ip} is valid")
        try:
            # Attempt to ping the IP address with a single packet
            subprocess.check_call(["ping", "-n", "1", ip])
            print(f"{ip} is pingable")
            file.writelines(f"{ip} Valid and Pingable\n")
        except subprocess.CalledProcessError:
            # The IP address is valid but not pingable
            print(f"{ip} is valid but not pingable")
            file.writelines(f"{ip} Valid but Not Pingable\n")
    else:
        print(f"{ip} is not valid. Skipping...")

file.close()  # Close the file after the loop

# Display the contents of the file
with open("ip_list.txt", "r") as file:
    contents = file.read()
    print("\nContents of ip_list.txt:")
    print(contents)

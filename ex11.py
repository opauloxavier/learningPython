print "Type you filename: \n"
file_again=raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
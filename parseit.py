#The file to parse the existing Document into a usable, readable format, such as TSV or JSON

#For each file in the exhibits list
  #For each line in file
    #if the line is parsed as \d\d\/\d\d
      #then create a new entry
    #else
      #Add the line to the current entry

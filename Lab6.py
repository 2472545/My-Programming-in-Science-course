# Step 6

dna = 'gctagctagctagcta' # We set the DNA strand
exons = [(0,3),(5,8)] # We set the location of the exons
annot = list(dna.lower()) # We make sure the DNA is lowercase
for s,e in exons: # We set a for loop
  for i in range(s,e): # We set another for loop 
    annot[i] = annot[i].upper() # We make the exons uppercase
print(''.join(annot)) # We join the exons back to the to the DNA strand, but in uppercase

# Step 7

dna = 'gctagctagctagcta' # We set the DNA strand
counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'} # We set the count to count how many of each letter is in the DNA strand
print(f"The count for every letter is as follows: {counts}") # We print the count for each letter

# Step 8

dna = 'gctagctagctagcta' # We set the DNA strand
print(f"The reverse of the DNA strand is as follows: {dna[::-1]}") # We print the reverse of the DNA strand 







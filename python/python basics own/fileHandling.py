
#type of data used for i/o 
     #text data like '1234' or 'hello' as a sequence of unicode characters unicode charactros are  like 
     #binary data like b'1234' or b'hello' as a sequence of bytes

#hence there are 2 types of data to deal with 
     #text files and binary files
     #text files -all program files are text files
     #binary files - all image files, audio files, video files are binary files


#file handling -> how file i/o is done in pyhotn or most languages
     #open a file
     #read or write to the file
     #close the file

#open a file
     #open() function is used to open a file
     #syntax: open(file, mode='r')
     #file - name of the file to open
     #mode - mode in which to open the file ther are 3 modes r,w,a 
     #r - read mode, w - write mode, a - append mode
     #default mode is read mode
     #returns a file object which is used to read or write to the file   
     

#write to a file
    #write() function is used to write to a file
    #syntax: file.write(data)
    #data - data to write to the file
    #returns the number of characters written to the file
    #write() function can only write strings to a file
    #writelines() function is used to write multiple lines to a file example
    #file.writelines(['hello\n', 'world\n'])


#read from a file
    #read() function is used to read from a file
    #syntax: file.read(size=-1)
    #size - number of bytes to read from the file
    #returns the data read from the file
    #if size is not specified, the entire file is read
    #read() function can only read strings from a file
    #readline() function is used to read a single line from a file example
    #file.readline() we can also read the upto n characters from the file using file.readline(n) 
    #readline( ) is automaticially changes teh line after reading the line like print statement

#close a file 
     # closing the file is a good practice after usage as it frees up the resources used by the file object
     #if we dont close the file the garbage collector will close the file when the program ends
     #syntax: file.close() 

#using context manager to close the file automatically the with keyword is used to create a context manager
    #syntax: with open(file, mode='r') as file:
    #file - name of the file to open
    #mode - mode in which to open the file
    #file is closed automatically when the block is exited


#to read/write binary files we need to specify the mode as 'rb' or 'wb' or 'ab' for read, write and append modes respectively
     #binary files are read/written in bytes instead of strings
     #we can even read image with the help of binary files
     #we can use the read() function to read the entire file or read(size) to read a specific number of bytes or we can also use the 
     #readline() function to read a single line from the file 

#file.seek() function is used to move the cursor to a specific position in the file
     #syntax: file.seek(offset, whence)
     #offset - number of bytes to move the cursor
     #whence - reference position to move the cursor
     #0 - start of the file, 1 - current position, 2 - end of the file
     #returns the new cursor position in the file

#file.tell() function is used to get the current cursor position in the file
     #syntax: file.tell()
     #returns the current cursor position in the file


#file.flush() function is used to flush the write buffer of the file
        #syntax: file.flush()
        #flushes the write buffer of the file
        #write buffer is the buffer that stores the data to be written to the file
        #flushing the write buffer writes the data to the file

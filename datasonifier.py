#########SOUNDSCAPESFINALPROJECT################
import matplotlib
import csv
import pandas as pd
import sys
import ly.musicxml.create_musicxml as create_musicxml

##loads csv as panda object and returns it given various parameters##
class data_to_assignment:
    
    def __init__(self, path, has_header, range_of_notes, diatonic):
        self.path = path
        self.has_header = has_header
        self.range_of_notes = range

        ##Set data to null at first
        self.parsed_data = None

        ##max should be set to Math.inf at some point
        self.x_max = 10000
        self.x_min = 0
        
        self.y_max = 10000
        self.y_min = 0

        ##intialize ranges (differences between max and min) to 0
        self.x_range = 0
        self.y_range = 0

        ##initialize note assignment arrays
        self.assignments = []

        ##get this from sys args
        self.range_of_notes = int(range_of_notes)

        self.diatonic = diatonic

        if(diatonic == "false"):
            self.notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        else:
            self.notes = ['C','D','E','F','G','A','B']
    def load_and_return_csv(self,path,has_header):
        if(has_header): self.parsed_data = pd.read_csv(path)
        else: self.parsed_data = pd.read_csv(path,header = None)

    ##used to get maxmiums of data##
    def get_maximums(self,data):
        self.x_max = data[0].max()
        self.y_max = data[1].max()

    ##used to get minimums of the data##
    def get_minimums(self,data):
        self.x_min = data[0].min()
        self.y_min = data[1].min()

    ##given max and min get the range in x
    def get_x_range(self,x_min,x_max):
        self.x_range =  x_max-x_min

    ##given max and min get the range in x
    def get_y_range(self,y_min,y_max):
        self.y_range = y_max-y_min

    def assign_data_to_note(self):
        self.load_and_return_csv(self.path,self.has_header)
        self.get_maximums(self.parsed_data)
        self.get_minimums(self.parsed_data)
        self.get_x_range(self.x_min,self.x_max)
        self.get_y_range(self.y_min,self.y_max)

        number_of_items = len(self.parsed_data[0])
        ##check to make sure every x value has a y value and vice versa
        assert (number_of_items == len(self.parsed_data[1])),\
        "please ensure every x value has a y value assigned"
        ##divide total range by the number of items to discretize note placements
        x_division = self.x_range/self.range_of_notes
        y_division = self.y_range/self.range_of_notes      
        current_pos_in_csv = 0
        for i in self.parsed_data[1]:           
            index = 1
            current_pos = self.y_min
            for j in range(int(self.x_range/x_division)):
                if(i >= current_pos and i <= current_pos + x_division):
                    self.assignments.append([i,index,self.parsed_data[0]\
                                             [current_pos_in_csv]])
                    break
                index += 1
                current_pos += x_division
                
            current_pos_in_csv += 1
        ## Error check to make sure every note has been assigned
        assert (number_of_items == len(self.assignments)),\
        "Failed to assign all data to note index sorry this is not your fault try different data"

    def assign_data_to_meter(self):
        for j in range(len(self.assignments)):
            if(j+1 <len(self.assignments)):
                ...
                #print(self.assignments[j+1][2]-self.assignments[j][2])
    def get_octave(self,assignment_val,note_length):
        return int(assignment_val/note_length)
        
    def give_me_the_data(self):
        self.assign_data_to_note()
        self.assign_data_to_meter()
        musxml = create_musicxml.CreateMusicXML()
        musxml.create_part()
        
        musxml.create_measure(mustime = [4,4], key = 0, divs=1)
        index = 0;
        for j in range(len(self.assignments)):
            index = index+1
            print(self.assignments[j][1])
            if(j+1 <len(self.assignments)):
                if(len(self.notes[self.assignments[j][1]%(len(self.notes))]) > 1):
                    musxml.new_note(self.notes[(self.assignments[j][1]%(len(self.notes)))-1],\
                    4 + (self.get_octave(self.assignments[j][1],(len(self.notes)))),\
                    'quarter',4,1)
                else:
                    musxml.new_note(self.notes[self.assignments[j][1]%(len(self.notes))],\
                    4 + (self.get_octave(self.assignments[j][1],(len(self.notes)))),\
                    'quarter',4)
            if(index%4 == 0):
                musxml.create_measure(divs=1)
            
            
        xml = musxml.musicxml()
        
        xml.write('your_generated_score.xml')
        
        return self.assignments
        
new_new = data_to_assignment(sys.argv[1],False,sys.argv[2],sys.argv[3])
new_new.give_me_the_data()



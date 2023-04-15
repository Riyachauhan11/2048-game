from tkinter import Frame,Label,CENTER

import Logics 
import Constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands={c.KEY_UP: Logics.move_up,c.KEY_DOWN: Logics.move_down,
                       c.KEY_LEFT: Logics.move_left,c.KEY_RIGHT: Logics.move_right}
        
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        #bg will be created inside the former frame we initialised
        background=Frame(self,bg=c.BACKGROUND_COLOUR_GAME,width=c.SIZE,height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                #cell will be created inside the bg frame
                cell=Frame(background,bg=c.BACKGROUND_COLOUR_CELL_EMPTY,
                           width=(c.SIZE/c.GRID_LEN),height=(c.SIZE/c.GRID_LEN))
                #in bg's grid at ith row and jth col we'll add cell 
                #with pad we have given gaps of 10 b/w cells
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)

                #inside cell(master)
                t=Label(master=cell,text="",bg=c.BACKGROUND_COLOUR_CELL_EMPTY,
                        justify=CENTER,font=c.FONT,width=5,height=2)
                #since cells are grid, we'll make the text grids as well to make use of grid functionality
                t.grid()

                #t gets appended as numbers will be changing with our moves
                grid_row.append(t)
            
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix=Logics.start_game()
        Logics.add_new_2(self.matrix)
        Logics.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOUR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),
                                                    bg=c.BACKGROUND_COLOR_DICT[new_number],
                                                    fg=c.CELL_COLOR_DICT[new_number])
        #it can take time to change colours and all
        #so it waits until all the changes have happened
        self.update_idletasks()

    def key_down(self,event):
        #gets the key pressed
        key=repr(event.char)
        if key in self.commands:
            #calling move_up/move_left/... func here while passing self.matrix as arg
            self.matrix,changed=self.commands[key](self.matrix)
            if changed:
                Logics.add_new_2(self.matrix)
                #updating the new cells from add_new_2 and move_up/move_left/... func
                self.update_grid_cells()
                changed=False
                if Logics.get_current_state(self.matrix)=='WON':
                    self.grid_cells[1][1].configure(text="You",
                                                    bg=c.BACKGROUND_COLOUR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!",
                                                    bg=c.BACKGROUND_COLOUR_CELL_EMPTY)
                if Logics.get_current_state(self.matrix)=='LOST':
                    self.grid_cells[1][1].configure(text="You",
                                                    bg=c.BACKGROUND_COLOUR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!",
                                                    bg=c.BACKGROUND_COLOUR_CELL_EMPTY)


gamegrid=Game2048()






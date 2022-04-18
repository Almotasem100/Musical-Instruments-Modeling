import numpy as np
import simpleaudio as sa
import sounddevice as sd
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import sys



class Musicar(Ui_MainWindow):
    def __init__(self,mainwindow):
        super(Musicar,self).setupUi(mainwindow)
        self.buttonslist=[self.c_note,self.csharp,self.d_note,
                          self.eflat,self.e_note,self.f_note,
                          self.fsharp,self.g_note,self.aflat,
                          self.a_note, self.bflat,self.b_note]
        self.c_note.setShortcut("a")
        self.d_note.setShortcut("s")
        self.e_note.setShortcut("d")
        self.f_note.setShortcut("f")
        self.g_note.setShortcut("g")
        self.b_note.setShortcut("j")
        self.a_note.setShortcut("h")
        self.csharp.setShortcut("q")
        self.eflat.setShortcut("w")
        self.fsharp.setShortcut("e")
        self.aflat.setShortcut("r")
        self.bflat.setShortcut("t")
        self.piano.setShortcut('Ctrl+p')
        self.guitar.setShortcut('Ctrl+g')
        # get tsteps for each sample, T is note duration in seconds
        self.sample_rate = 44100
        self.T = 4
        self.t = np.linspace(0, self.T, int(self.T * self.sample_rate), False)

        # calculate note frequencies
        self.notes_range = np.arange(-9, 3)
        self.A_freq = 440

        self.notes_freq = np.zeros(12)
        self.piano_notes= [0]*12
        self.guitar_notes=[0]*12

        #generate from C4 notes(middle c) to B4
        for i in range(len(self.notes_range)):
            self.notes_freq[i] = self.A_freq * 2 ** (self.notes_range[i] / 12)



        self.playnotes=[lambda: self.playEachNote(0),lambda:self.playEachNote(1),lambda:self.playEachNote(2),
                        lambda:self.playEachNote(3),lambda:self.playEachNote(4),lambda:self.playEachNote(5),
                        lambda:self.playEachNote(6),lambda:self.playEachNote(7),lambda:self.playEachNote(8),
                        lambda:self.playEachNote(9),lambda:self.playEachNote(10),lambda: self.playEachNote(11)]

        for i in range(12):
            self.buttonslist[i].clicked.connect(self.playnotes[i])  

        self.slider.setMaximum(5)
        self.slider.setMinimum(1)
        self.slider.setSingleStep(.5)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.sustain) 
        
        self.piano_play()
        self.guitar_play()

    def sustain(self):
        self.T=self.slider.value()
        self.piano_play()
        self.guitar_play()
        print(self.T)
    def piano_play(self):
        for i in range(12):
            self.piano_notes[i] = 0.6 * np.sin(2 * np.pi * self.notes_freq[i] * self.t) * np.exp(-0.0015 * np.pi * self.notes_freq[i] * self.t)
            self.piano_notes[i] += 0.4 * np.sin(2 * np.pi * self.notes_freq[i] * self.t) * np.exp(-0.0015 * np.pi * self.notes_freq[i] * self.t)
            # for saturated sound
            self.piano_notes[i] += self.piano_notes[i] * self.piano_notes[i] * self.piano_notes[i]
            self.piano_notes[i] *= 1 + 16 * self.t * np.exp(-6 * self.t)
            # normalize to 16-bit range
            self.piano_notes[i] *= 32767 / np.max(np.abs(self.piano_notes[i]))
            # converself.t to 16-bit data
            self.piano_notes[i] = self.piano_notes[i].astype(np.int16)

    
    def playEachNote(self, i):
        if self.piano.isChecked() == True:
            play_obj = sa.play_buffer(self.piano_notes[i], 1, 2, self.sample_rate)
        elif self.guitar.isChecked() ==True:
            sd.play(self.guitar_notes[i],samplerate=self.sample_rate)


    def karplus_strong(self, wavetable, n_samples):
        samples = []
        current_sample = 0
        previous_value = 0
        while len(samples) < n_samples:
            wavetable[current_sample] = 0.5 * (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % wavetable.size
        return np.array(samples)

    def guitar_play(self):
        for i in range(12):
            wavetable_size = self.sample_rate // int(self.notes_freq[i])
            wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
            sample = self.karplus_strong(wavetable, self.T * self.sample_rate)
            self.guitar_notes[i]=sample


def main():
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Musicar(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
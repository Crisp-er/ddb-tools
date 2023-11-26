# -*- coding: utf-8 -*-
import threading

import wx
import wx.xrc

import SplashModule
import mixins_ddb
import pack_ddb


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title="DDB Toolbox",
            pos=wx.DefaultPosition,
            size=wx.Size(600, 500),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.Size(600, 500), wx.Size(600, 500))
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX)

        #icon = wx.Icon(name="./resources/icon.ico", type=wx.BITMAP_TYPE_ICO)
        #self.SetIcon(icon)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1 = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, "Pack from a dev vb"), wx.VERTICAL
        )

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(
            sbSizer1.GetStaticBox(),
            wx.ID_ANY,
            ".tree file:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText1.Wrap(-1)

        bSizer10.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_filePicker1 = wx.FilePickerCtrl(
            sbSizer1.GetStaticBox(),
            wx.ID_ANY,
            wx.EmptyString,
            "Select a file",
            "*.tree",
            wx.DefaultPosition,
            wx.Size(500, -1),
            wx.FLP_DEFAULT_STYLE,
        )
        bSizer10.Add(self.m_filePicker1, 0, wx.ALL, 5)

        sbSizer1.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer101 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(
            sbSizer1.GetStaticBox(),
            wx.ID_ANY,
            "destination path (optional):",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText11.Wrap(-1)

        bSizer101.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.m_dirPicker1 = wx.DirPickerCtrl(
            sbSizer1.GetStaticBox(),
            wx.ID_ANY,
            wx.EmptyString,
            "Select a folder",
            wx.DefaultPosition,
            wx.Size(500, -1),
            wx.DIRP_DEFAULT_STYLE,
        )
        bSizer101.Add(self.m_dirPicker1, 0, wx.ALL, 5)

        sbSizer1.Add(bSizer101, 1, wx.EXPAND, 5)

        bSizer1.Add(sbSizer1, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_toggleBtn2 = wx.ToggleButton(
            self, wx.ID_ANY, "Process", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer6.Add(self.m_toggleBtn2, 0, wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)

        self.m_gauge11 = wx.Gauge(
            self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(600, -1), wx.GA_HORIZONTAL
        )
        self.m_gauge11.SetValue(0)
        bSizer51.Add(self.m_gauge11, 0, wx.ALL, 5)

        bSizer1.Add(bSizer51, 1, wx.EXPAND, 5)

        sbSizer2 = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, "Mixins"), wx.VERTICAL
        )

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(
            sbSizer2.GetStaticBox(),
            wx.ID_ANY,
            "source .ddi file:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText2.Wrap(-1)

        bSizer8.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_filePicker2 = wx.FilePickerCtrl(
            sbSizer2.GetStaticBox(),
            wx.ID_ANY,
            wx.EmptyString,
            "Select a file",
            "*.ddi",
            wx.DefaultPosition,
            wx.Size(500, -1),
            wx.FLP_DEFAULT_STYLE,
        )
        bSizer8.Add(self.m_filePicker2, 0, wx.ALL, 5)

        sbSizer2.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(
            sbSizer2.GetStaticBox(),
            wx.ID_ANY,
            "mixins .ddi file:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText3.Wrap(-1)

        bSizer9.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_filePicker3 = wx.FilePickerCtrl(
            sbSizer2.GetStaticBox(),
            wx.ID_ANY,
            wx.EmptyString,
            "Select a file",
            "*.ddi",
            wx.DefaultPosition,
            wx.Size(500, -1),
            wx.FLP_DEFAULT_STYLE,
        )
        bSizer9.Add(self.m_filePicker3, 0, wx.ALL, 5)

        sbSizer2.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer1011 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText111 = wx.StaticText(
            sbSizer2.GetStaticBox(),
            wx.ID_ANY,
            "destination path (optional):",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText111.Wrap(-1)

        bSizer1011.Add(self.m_staticText111, 0, wx.ALL, 5)

        self.m_dirPicker11 = wx.DirPickerCtrl(
            sbSizer2.GetStaticBox(),
            wx.ID_ANY,
            wx.EmptyString,
            "Select a folder",
            wx.DefaultPosition,
            wx.Size(500, -1),
            wx.DIRP_DEFAULT_STYLE,
        )
        bSizer1011.Add(self.m_dirPicker11, 0, wx.ALL, 5)

        sbSizer2.Add(bSizer1011, 1, wx.EXPAND, 5)

        bSizer1012 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText112 = wx.StaticText(
            sbSizer2.GetStaticBox(),
            wx.ID_ANY,
            "mixins items (optional):",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText112.Wrap(-1)

        bSizer1012.Add(self.m_staticText112, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(
            sbSizer2.GetStaticBox(),
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(500, -1),
            0,
        )
        bSizer1012.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        sbSizer2.Add(bSizer1012, 1, wx.EXPAND, 5)

        bSizer1.Add(sbSizer2, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_toggleBtn1 = wx.ToggleButton(
            self, wx.ID_ANY, "Process", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer4.Add(self.m_toggleBtn1, 0, wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_gauge1 = wx.Gauge(
            self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(600, -1), wx.GA_HORIZONTAL
        )
        self.m_gauge1.SetValue(0)
        bSizer5.Add(self.m_gauge1, 0, wx.ALL, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_toggleBtn2.Bind(wx.EVT_TOGGLEBUTTON, self.pack)
        self.m_toggleBtn1.Bind(wx.EVT_TOGGLEBUTTON, self.mixins)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def pack(self, event):
        self.m_gauge11.SetValue(0)
        self.m_gauge11.Pulse()
        self.m_toggleBtn2.Enable(False)
        self.m_toggleBtn1.Enable(False)
        self.m_filePicker1.Enable(False)
        self.m_dirPicker1.Enable(False)
        self.m_filePicker2.Enable(False)
        self.m_filePicker3.Enable(False)
        self.m_dirPicker11.Enable(False)
        self.m_textCtrl1.Enable(False)
        src_path = self.m_filePicker1.GetPath()
        dst_path = self.m_dirPicker1.GetPath()
        event1 = threading.Event()
        event2 = threading.Event()

        def packDDB(src_path, dst_path):
            try:
                if dst_path == "":
                    pack_ddb.main(["--src_path", src_path])
                else:
                    pack_ddb.main(["--src_path", src_path, "--dst_path", dst_path])
            except Exception as e:
                global eramessage
                eramessage = e
                event2.set()
            finally:
                event1.set()

        threadPack = threading.Thread(target=packDDB, args=(src_path, dst_path))
        threadPack.daemon = True
        threadPack.start()

        def kanzen():
            event1.wait()
            self.m_toggleBtn2.Enable(True)
            self.m_toggleBtn1.Enable(True)
            self.m_filePicker1.Enable(True)
            self.m_dirPicker1.Enable(True)
            self.m_filePicker2.Enable(True)
            self.m_filePicker3.Enable(True)
            self.m_dirPicker11.Enable(True)
            self.m_textCtrl1.Enable(True)
            if event2.is_set():
                self.m_gauge11.SetValue(0)
                wx.MessageBox(
                    "Error: " + str(eramessage), "Error", wx.OK | wx.ICON_ERROR
                )
            else:
                self.m_gauge11.SetValue(100)
                wx.MessageBox("Success", "Success", wx.OK | wx.ICON_INFORMATION)

        threadkanzen = threading.Thread(target=kanzen)
        threadkanzen.daemon = True
        threadkanzen.start()
        event.Skip()

    def mixins(self, event):
        self.m_gauge1.SetValue(0)
        self.m_gauge1.Pulse()
        self.m_toggleBtn2.Enable(False)
        self.m_toggleBtn1.Enable(False)
        self.m_filePicker1.Enable(False)
        self.m_dirPicker1.Enable(False)
        self.m_filePicker2.Enable(False)
        self.m_filePicker3.Enable(False)
        self.m_dirPicker11.Enable(False)
        self.m_textCtrl1.Enable(False)
        src_path = self.m_filePicker2.GetPath()
        mixins_path = self.m_filePicker3.GetPath()
        dst_path = self.m_dirPicker11.GetPath()
        mixins_items = self.m_textCtrl1.GetValue()
        event3 = threading.Event()
        event4 = threading.Event()

        def mixinsDDB(src_path, mixins_path, dst_path, mixins_items):
            try:
                if dst_path == "":
                    mixins_ddb.main(
                        [
                            "--src_path",
                            src_path,
                            "--mixins_path",
                            mixins_path,
                            "--mixins_items",
                            mixins_items,
                        ]
                    )
                elif mixins_items == "":
                    mixins_ddb.main(
                        [
                            "--src_path",
                            src_path,
                            "--mixins_path",
                            mixins_path,
                            "--dst_path",
                            dst_path,
                        ]
                    )
                elif dst_path == "" and mixins_items == "":
                    mixins_ddb.main(
                        ["--src_path", src_path, "--mixins_path", mixins_path]
                    )
                else:
                    mixins_ddb.main(
                        [
                            "--src_path",
                            src_path,
                            "--mixins_path",
                            mixins_path,
                            "--dst_path",
                            dst_path,
                            "--mixins_items",
                            mixins_items,
                        ]
                    )
            except Exception as e:
                global eramessage
                eramessage = e
                event4.set()
            finally:
                event3.set()

        threadMixins = threading.Thread(
            target=mixinsDDB, args=(src_path, mixins_path, dst_path, mixins_items)
        )
        threadMixins.daemon = True
        threadMixins.start()

        def kanzen2():
            event3.wait()
            self.m_toggleBtn2.Enable(True)
            self.m_toggleBtn1.Enable(True)
            self.m_filePicker1.Enable(True)
            self.m_dirPicker1.Enable(True)
            self.m_filePicker2.Enable(True)
            self.m_filePicker3.Enable(True)
            self.m_dirPicker11.Enable(True)
            self.m_textCtrl1.Enable(True)
            if event4.is_set():
                self.m_gauge1.SetValue(0)
                wx.MessageBox(
                    "Error: " + str(eramessage), "Error", wx.OK | wx.ICON_ERROR
                )
            else:
                self.m_gauge1.SetValue(100)
                wx.MessageBox("Success", "Success", wx.OK | wx.ICON_INFORMATION)

        threadkanzen2 = threading.Thread(target=kanzen2)
        threadkanzen2.daemon = True
        threadkanzen2.start()
        event.Skip()


try:
    app = wx.App()
    window = MyFrame1(parent=None)
    window.Show()
    app.MainLoop()
except Exception as e:
    if str(e) != (
        'C++ assertion ""GetWindow() != 0"" failed at ..\..\src\common\wincmn.cpp(3998) in '
        "wxWindowAccessible::GetDescription(): "
    ):
        wx.MessageBox("Error: " + str(e), "Error", wx.OK | wx.ICON_ERROR)

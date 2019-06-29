"""
This is file pscm.py, then this string, being the
first statement in the file, will become the "parser" module's
docstring when the file is imported.
"""
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
# from functools import reduce
pd.__version__


class PsCm(object):
    def parser():
        """
        Parser Function.
        """
        print(os.getcwd())

        os.chdir('/Users/ylmrdm/mlio/data/raw')

        excel_file = 'Exp2StraceBTIOckpt1n1.xlsx'

        xlsx = pd.ExcelFile(excel_file)

        strace_sheets = []
        for sheet in xlsx.sheet_names:
            strace_sheets.append(xlsx.parse(sheet))
        strace_sheets = pd.read_excel(excel_file, sheet_name=None, header=None, skiprows=1)
        strace = pd.concat(strace_sheets, sort=False)

        strace.head()

        strace["pid"] = strace[0]
        strace["time"] = strace[1]
        strace["operation"] = strace[2]
        strace.drop(columns=[0, 1, 2, 3, 4, 5], inplace=True)

        strace.head()

        pid_open_list = list()
        time_open_list = list()
        operation_open_list = list()
        pid_write_list = list()
        time_write_list = list()
        operation_write_list = list()
        pid_read_list = list()
        time_read_list = list()
        operation_read_list = list()
        pid_close_list = list()
        time_close_list = list()
        operation_close_list = list()

        list_counter = 0

        for i in range(0, len(strace)):
            if 'open' in strace["operation"][i]:
                pid_open_list.append(strace["pid"][i])
                time_open_list.append(strace["time"][i])
                operation_open_list.append(strace["operation"][i])
            elif 'write' in strace["operation"][i]:
                pid_write_list.append(strace["pid"][i])
                time_write_list.append(strace["time"][i])
                operation_write_list.append(strace["operation"][i])
            elif 'read' in strace["operation"][i]:
                pid_read_list.append(strace["pid"][i])
                time_read_list.append(strace["time"][i])
                operation_read_list.append(strace["operation"][i])
            elif 'close' in strace["operation"][i]:
                pid_close_list.append(strace["pid"][i])
                time_close_list.append(strace["time"][i])
                operation_close_list.append(strace["operation"][i])
            else:
                list_counter = list_counter + 1
        # print(list_counter)

        strace_o = pd.DataFrame({'pid': pid_open_list, 'time': time_open_list,
                                 'operation': operation_open_list})
        strace_o.to_excel(r'raw_open.xlsx', index=False, engine='xlsxwriter')
        strace_w = pd.DataFrame({'pid': pid_write_list, 'time': time_write_list,
                                 'operation': operation_write_list})
        strace_w.to_excel(r'raw_write.xlsx', index=False, engine='xlsxwriter')
        strace_r = pd.DataFrame({'pid': pid_read_list, 'time': time_read_list,
                                 'operation': operation_read_list})
        strace_r.to_excel(r'raw_read.xlsx', index=False, engine='xlsxwriter')
        strace_c = pd.DataFrame({'pid': pid_close_list, 'time': time_close_list,
                                 'operation': operation_close_list})
        strace_c.to_excel(r'raw_close.xlsx', index=False, engine='xlsxwriter')

        print("Total open datas: \n", strace['operation'].str.contains('open').value_counts())

        print("Total read datas: \n", strace['operation'].str.contains('read').value_counts())

        print("Total write datas: \n", strace['operation'].str.contains('write').value_counts())

        print("Total close datas: \n", strace['operation'].str.contains('close').value_counts())

    def separator():
        """
        Separator Function.
        """
        os.chdir("/Users/ylmrdm/mlio/data/raw")

        file_open = 'raw_open.xlsx'
        file_read = 'raw_read.xlsx'
        file_write = 'raw_write.xlsx'
        file_close = 'raw_close.xlsx'

        # Defining the sheet from open.xlsx
        xlsx_open = pd.ExcelFile(file_open)
        print(type(xlsx_open))
        open_sheets = []
        for sheet in xlsx_open.sheet_names:
            open_sheets.append(xlsx_open.parse(sheet))
        open_sheets = pd.read_excel(file_open, sheet_name=None, header=None, skiprows=1)
        open = pd.concat(open_sheets, sort=False)
        open.head()

        # Defining the sheet from read.xlsx
        xlsx_read = pd.ExcelFile(file_read)
        print(type(xlsx_read))
        read_sheets = []
        for sheet in xlsx_read.sheet_names:
            read_sheets.append(xlsx_read.parse(sheet))
        read_sheets = pd.read_excel(file_read, sheet_name=None, header=None, skiprows=1)
        read = pd.concat(read_sheets, sort=False)
        read.head()

        # Defining the sheet from write.xlsx
        xlsx_write = pd.ExcelFile(file_write)
        print(type(xlsx_write))
        write_sheets = []
        for sheet in xlsx_write.sheet_names:
            write_sheets.append(xlsx_write.parse(sheet))
        write_sheets = pd.read_excel(file_write, sheet_name=None, header=None, skiprows=1)
        write = pd.concat(write_sheets, sort=False)
        write.head()

        # Defining the sheet from close.xlsx
        xlsx_close = pd.ExcelFile(file_close)
        print(type(xlsx_close))
        close_sheets = []
        for sheet in xlsx_close.sheet_names:
            close_sheets.append(xlsx_close.parse(sheet))
        close_sheets = pd.read_excel(file_close, sheet_name=None, header=None, skiprows=1)
        close = pd.concat(close_sheets, sort=False)
        close.head()

        # Changing the column names
        open.columns = ['pid', 'time', 'operation']
        read.columns = ['pid', 'time', 'operation']
        write.columns = ['pid', 'time', 'operation']
        close.columns = ['pid', 'time', 'operation']
        open.to_excel('raw_open.xlsx', index=False, engine='xlsxwriter')
        read.to_excel('raw_read.xlsx', index=False, engine='xlsxwriter')
        write.to_excel('raw_write.xlsx', index=False, engine='xlsxwriter')
        close.to_excel('raw_close.xlsx', index=False, engine='xlsxwriter')

        os.chdir("/Users/ylmrdm/mlio/data/external")

        # ------------------------------------ OPEN ----------------------------------------
        # ---------------------------------- OPENMIXED -------------------------------------
        # Relationship btw unfinished and resumed processes to merge them for openmixed.xlsx
        pid_openuf_list = list()
        time_openuf_list = list()
        operation_openuf_list = list()
        pid_openres_list = list()
        time_openres_list = list()
        operation_openres_list = list()

        open_counter = 0
        for i in range(0, len(open)):
            if 'unfinished' in open["operation"][i]:
                pid_openuf_list.append(open["pid"][i])
                time_openuf_list.append(open["time"][i])
                operation_openuf_list.append(open["operation"][i])
            elif 'open resumed' in open['operation'][i]:
                pid_openres_list.append(open["pid"][i])
                time_openres_list.append(open["time"][i])
                operation_openres_list.append(open["operation"][i])
            else:
                open_counter = open_counter + 1
        print(open_counter)

        openuf = pd.DataFrame({'pid': pid_openuf_list, 'time': time_openuf_list,
                               'operation': operation_openuf_list})
        openres = pd.DataFrame({'pid': pid_openres_list, 'time': time_openres_list,
                                'operation': operation_openres_list})

        new = openres["operation"].str.split("=", n=1, expand=True)
        openres["operation"] = new[0]
        openres["idfile"] = new[1]

        openmixed = openuf.combine_first(openres)  # combine_first() fuction for openmixed.

        # Separating columns to make another columns from openmixed.xlsx
        new = openmixed["operation"].str.split("(", n=1, expand=True)
        openmixed["operation"] = new[0]
        openmixed["path"] = new[1]
        openmixed.to_excel('openmixed.xlsx', index=False, engine='xlsxwriter')
        new = openmixed["path"].str.split(" ", n=1, expand=True)
        openmixed["path"] = new[0]
        openmixed["flag"] = new[1]
        openmixed["flag"] = openmixed["flag"].str.replace('<unfinished ...>', '')
        openmixed["flag"] = openmixed["flag"].str.replace(',', '').str.replace('0600', '')
        openmixed["path"] = openmixed["path"].str.replace('"', '').str.replace(',', '')
        openmixed["idfile"] = openmixed["idfile"].str.lstrip(' ')
        new = openmixed["idfile"].str.split(" ", n=1, expand=True)
        openmixed["idfile"] = new[0]
        openmixed["error"] = new[1]
        openmixed.to_excel('openmixed.xlsx', index=False, engine='xlsxwriter')

        open["operation"].str.contains("unfinished").value_counts()

        # ---------------------------------- OPENPURE -------------------------------------
        # Relationship btw unfinished and resumed processes to merge them for openpure.xlsx

        pid_pure_open = list()
        time_pure_open = list()
        operation_pure_open = list()

        unwanted_counter = 0
        for i in range(0, len(open)):
            if 'unfinished' not in open["operation"][i] and 'resumed' not in open["operation"][i]:
                pid_pure_open.append(open["pid"][i])
                time_pure_open.append(open["time"][i])
                operation_pure_open.append(open["operation"][i])
            else:
                unwanted_counter = unwanted_counter + 1
        print(unwanted_counter)

        openpure = pd.DataFrame({'pid': pid_pure_open, 'time': time_pure_open,
                                 'operation': operation_pure_open})

        open["operation"].str.contains('open').value_counts()
        openpure.to_excel('openpure.xlsx', index=False, engine='xlsxwriter')

        # Separating columns to make another columns from openpure.xlsx
        new = openpure["operation"].str.split("(", n=1, expand=True)
        openpure["operation"] = new[0]
        openpure["path"] = new[1]
        new = openpure["path"].str.split('=', n=1, expand=True)
        openpure["path"] = new[0]
        openpure["idfile"] = new[1]
        openpure["idfile"] = openpure["idfile"].str.lstrip(' ')
        new = openpure["idfile"].str.split(" ", n=1, expand=True)
        openpure["idfile"] = new[0]
        openpure["error"] = new[1]
        new = openpure["path"].str.split(" ", n=1, expand=True)
        openpure["path"] = new[0]
        openpure["flag"] = new[1]
        openpure["path"] = openpure["path"].str.replace('"', '').str.replace(',', '')
        openpure["flag"] = openpure["flag"].str.replace(')', '').str.replace(',', '')
        openpure["flag"] = openpure["flag"].str.replace('0600', '').str.replace('0666', '')
        openpure.to_excel('openpure.xlsx', index=False, engine='xlsxwriter')

        openpure = openpure[['pid', 'time', 'operation', 'path', 'idfile', 'flag', 'error']]
        openmixed = openmixed[['pid', 'time', 'operation', 'path', 'idfile', 'flag', 'error']]

        openpure.to_excel('openpure.xlsx', index=False, engine='xlsxwriter')
        openmixed.to_excel('openmixed.xlsx', index=False, engine='xlsxwriter')

        # Concatenating with openmixed and openpure to make just one excel file from them called as open.xlsx
        # This file(open.xlsx) will keep inside ./output/data folder.
        open = pd.concat([openmixed, openpure])
        open["operation"].str.contains('open').value_counts()

        os.chdir("/Users/ylmrdm/mlio/data/interim")

        open.to_excel('open.xlsx', index=False, engine='xlsxwriter')

        os.chdir("/Users/ylmrdm/mlio/data/external")
        # ------------------------------------ READ ----------------------------------------
        # ---------------------------------- READMIXED -------------------------------------
        # Relationship btw unfinished and resumed processes to merge them for readmixed.xlsx

        pid_read_unfinished = list()
        time_read_unfinished = list()
        operation_read_unfinished = list()

        pid_read_resumed = list()
        time_read_resumed = list()
        operation_read_resumed = list()

        read_counter = 0
        for i in range(0, len(read)):
            if 'unfinished' in read["operation"][i]:
                pid_read_unfinished.append(read["pid"][i])
                time_read_unfinished.append(read["time"][i])
                operation_read_unfinished.append(read["operation"][i])
            elif 'read resumed' in read['operation'][i]:
                pid_read_resumed.append(read["pid"][i])
                time_read_resumed.append(read["time"][i])
                operation_read_resumed.append(read["operation"][i])
            else:
                read_counter = read_counter + 1
        print(read_counter)

        readuf = pd.DataFrame({'pid': pid_read_unfinished, 'time': time_read_unfinished,
                               'operation': operation_read_unfinished})
        readres = pd.DataFrame({'pid': pid_read_resumed, 'time': time_read_resumed,
                                'operation': operation_read_resumed})

        # read["operation"].str.contains('open').value_counts()
        # read["operation"].str.contains('unfinished').value_counts()
        # read["operation"].str.contains('read resumed').value_counts()

        new = readuf["operation"].str.split(",", n=1, expand=True)
        readuf["operation"] = new[0]
        readuf["path"] = new[1]
        new = readuf["operation"].str.split("(", n=1, expand=True)
        readuf["operation"] = new[0]
        readuf["idfile"] = new[1]
        # readuf.to_excel('readuf.xlsx', index=False, engine='xlsxwriter')

        new = readres["operation"].str.split('>', n=1, expand=True)
        readres["operation"] = new[0]
        readres["path"] = new[1]
        new = readres["path"].str.rsplit(',', n=1, expand=True)
        readres["path"] = new[0]
        readres["rs"] = new[1]
        readres['path'] = readres["path"].str.replace('"', '')
        readres['operation'] = readres["operation"].str.replace('<', '').str.replace('resumed', '')
        readres['operation'] = readres["operation"].str.replace('.', '')
        new = readres["rs"].str.split('=', n=1, expand=True)
        readres["rs"] = new[0]
        readres["size"] = new[1]
        readres['rs'] = readres["rs"].str.replace(')', '')
        readres["size"] = readres["size"].str.lstrip(' ')
        new = readres["size"].str.split(' ', n=1, expand=True)
        readres["size"] = new[0]
        readres["error"] = new[1]
        # readres.to_excel('readres.xlsx', index=False, engine='xlsxwriter')

        readmixed = readres.combine_first(readuf)  # combine_first() fuction for readmixed.

        readmixed.to_excel('readmixed.xlsx', index=False, engine='xlsxwriter')

        # ---------------------------------- READPURE -------------------------------------
        # Relationship btw unfinished and resumed processes to merge them for readpure.xlsx

        pid_pure_read = list()
        time_pure_read = list()
        operation_pure_read = list()

        unwanted_counter = 0
        for i in range(0, len(read)):
            if 'unfinished' not in read["operation"][i] and 'resumed' not in read["operation"][i]:
                pid_pure_read.append(read["pid"][i])
                time_pure_read.append(read["time"][i])
                operation_pure_read.append(read["operation"][i])
            else:
                unwanted_counter = unwanted_counter + 1
        print(unwanted_counter)

        readpure = pd.DataFrame({'pid': pid_pure_read, 'time': time_pure_read,
                                 'operation': operation_pure_read})

        readpure.to_excel('readpure.xlsx', index=False, engine='xlsxwriter')

        # Changing the dataframe from read to readpure..
        new = readpure["operation"].str.split("(", n=1, expand=True)
        readpure["operation"] = new[0]
        readpure["path"] = new[1]
        new = readpure["path"].str.split(',', n=1, expand=True)
        readpure["idfile"] = new[0]
        readpure["path"] = new[1]
        new = readpure["path"].str.rsplit(",", n=1, expand=True)
        readpure["path"] = new[0]
        readpure["rs"] = new[1]
        new = readpure["rs"].str.split("=", n=1, expand=True)
        readpure["rs"] = new[0]
        readpure["size"] = new[1]
        readpure["size"] = readpure["size"].str.lstrip(' ')
        readpure["rs"] = readpure["rs"].str.replace(')', '')
        new = readpure["size"].str.split(" ", n=1, expand=True)
        readpure["size"] = new[0]
        readpure["error"] = new[1]
        readpure["path"] = readpure["path"].str.replace('"', '')
        readpure.to_excel('readpure.xlsx', index=False, engine='xlsxwriter')

        readpure = readpure[['pid', 'time', 'operation', 'path', 'idfile', 'rs', 'size', 'error']]
        readmixed = readmixed[['pid', 'time', 'operation', 'path', 'idfile', 'rs', 'size', 'error']]

        readpure.to_excel('readpure.xlsx', index=False, engine='xlsxwriter')
        readmixed.to_excel('readmixed.xlsx', index=False, engine='xlsxwriter')

        # Concatenating with readmixed and readpure to make just one excel file from them called as read.xlsx
        # This file(read.xlsx) will keep inside ./output/data folder.
        read = pd.concat([readmixed, readpure])

        read["operation"].str.contains('read').value_counts()

        os.chdir("/Users/ylmrdm/mlio/data/interim")

        read.to_excel('read.xlsx', index=False, engine='xlsxwriter')

        os.chdir("/Users/ylmrdm/mlio/data/external")
        # read["error"].str.contains('').value_counts()

        # ------------------------------------ WRITE ----------------------------------------
        # ---------------------------------- WRITEMIXED -------------------------------------
        # Relationship btw unfinished and resumed processes to merge them for writemixed.xlsx

        pid_write_unfinished = list()
        time_write_unfinished = list()
        operation_write_unfinished = list()

        pid_write_resumed = list()
        time_write_resumed = list()
        operation_write_resumed = list()

        write_counter = 0
        for i in range(0, len(write)):
            if 'unfinished' in write["operation"][i]:
                pid_write_unfinished.append(write["pid"][i])
                time_write_unfinished.append(write["time"][i])
                operation_write_unfinished.append(write["operation"][i])
            elif 'write resumed' in write['operation'][i]:
                pid_write_resumed.append(write["pid"][i])
                time_write_resumed.append(write["time"][i])
                operation_write_resumed.append(write["operation"][i])
            else:
                write_counter = write_counter + 1
        print(write_counter)

        writeuf = pd.DataFrame({'pid': pid_write_unfinished, 'time': time_write_unfinished,
                                'operation': operation_write_unfinished})
        writeres = pd.DataFrame({'pid': pid_write_resumed, 'time': time_write_resumed,
                                 'operation': operation_write_resumed})

        # write["operation"].str.contains('open').value_counts()
        # write["operation"].str.contains('unfinished').value_counts()
        # write["operation"].str.contains('write resumed').value_counts()

        new = writeuf["operation"].str.split("(", n=1, expand=True)
        writeuf["operation"] = new[0]
        writeuf["path"] = new[1]
        new = writeuf["path"].str.split(",", n=1, expand=True)
        writeuf["idfile"] = new[0]
        writeuf["path"] = new[1]
        new = writeuf["path"].str.rsplit('"', n=1, expand=True)
        writeuf["path"] = new[0]
        writeuf["rs"] = new[1]
        writeuf["rs"] = writeuf["rs"].str.replace('<unfinished', '').str.replace('.', '')
        writeuf["rs"] = writeuf["rs"].str.replace('>', '').str.replace(',', '')
        writeuf["rs"] = writeuf["rs"].str.lstrip(' ')
        writeuf["path"] = writeuf["path"].str.replace('"', '')
        # writeuf.to_excel('writeuf.xlsx', index=False, engine='xlsxwriter')

        new = writeres["operation"].str.split('>', n=1, expand=True)
        writeres["operation"] = new[0]
        writeres["size"] = new[1]
        writeres["operation"] = writeres["operation"].str.replace('<', '').str.replace('.', '')
        writeres["operation"] = writeres["operation"].str.replace('resumed', '')
        writeres["operation"] = writeres["operation"].str.lstrip(' ')
        writeres["size"] = writeres["size"].str.replace(')', '').str.replace('=', '')
        writeres["size"] = writeres["size"].str.lstrip(' ')
        # writeres.to_excel('writeres.xlsx', index=False, engine='xlsxwriter')

        writemixed = writeres.combine_first(writeuf)  # combine_first() fuction for writemixed.

        writemixed.to_excel('writemixed.xlsx', index=False, engine='xlsxwriter')

        # ---------------------------------- WRITEPURE-------------------------------------
        # Relationship btw unfinished and resumed processes to merge them for writepure.xlsx

        pid_pure_write = list()
        time_pure_write = list()
        operation_pure_write = list()

        unwanted_counter = 0
        for i in range(0, len(write)):
            if 'unfinished' not in write["operation"][i] and 'resumed' not in write["operation"][i]:
                pid_pure_write.append(write["pid"][i])
                time_pure_write.append(write["time"][i])
                operation_pure_write.append(write["operation"][i])
            else:
                unwanted_counter = unwanted_counter + 1
        print(unwanted_counter)

        writepure = pd.DataFrame({'pid': pid_pure_write, 'time': time_pure_write,
                                  'operation': operation_pure_write})

        writepure.to_excel('writepure.xlsx', index=False, engine='xlsxwriter')

        # Changing the dataframe from write to writepure..
        new = writepure["operation"].str.split("(", n=1, expand=True)
        writepure["operation"] = new[0]
        writepure["path"] = new[1]
        new = writepure["path"].str.split(',', n=1, expand=True)
        writepure["idfile"] = new[0]
        writepure["path"] = new[1]
        new = writepure["path"].str.rsplit(",", n=1, expand=True)
        writepure["path"] = new[0]
        writepure["rs"] = new[1]
        new = writepure["rs"].str.split("=", n=1, expand=True)
        writepure["rs"] = new[0]
        writepure["size"] = new[1]
        writepure["size"] = writepure["size"].str.lstrip(' ')
        writepure["rs"] = writepure["rs"].str.replace(')', '')
        writepure["path"] = writepure["path"].str.replace('"', '')
        writepure["rs"] = writepure["rs"].str.lstrip(' ')
        writepure.to_excel('writepure.xlsx', index=False, engine='xlsxwriter')

        writepure = writepure[['pid', 'time', 'operation', 'path', 'idfile', 'rs', 'size']]
        writemixed = writemixed[['pid', 'time', 'operation', 'path', 'idfile', 'rs', 'size']]

        writepure.to_excel('writepure.xlsx', index=False, engine='xlsxwriter')
        writemixed.to_excel('writemixed.xlsx', index=False, engine='xlsxwriter')

        # Concatenating with writemixed and writepure to make just one excel file from them called as write.xlsx
        # This file(write.xlsx) will keep inside ./output/data folder.
        write = pd.concat([writemixed, writepure])

        write["operation"].str.contains('write').value_counts()

        os.chdir("/Users/ylmrdm/mlio/data/interim")

        write.to_excel('write.xlsx', index=False, engine='xlsxwriter')

        os.chdir("/Users/ylmrdm/mlio/data/external")
        # ------------------------------------ CLOSE ----------------------------------------
        # ---------------------------------- CLOSEMIXED -------------------------------------
        # Relationship btw unfinished and resumed processes to merge them for closemixed.xlsx

        pid_close_unfinished = list()
        time_close_unfinished = list()
        operation_close_unfinished = list()
        pid_close_resumed = list()
        time_close_resumed = list()
        operation_close_resumed = list()

        close_counter = 0
        for i in range(0, len(close)):
            if 'unfinished' in close["operation"][i]:
                pid_close_unfinished.append(close["pid"][i])
                time_close_unfinished.append(close["time"][i])
                operation_close_unfinished.append(close["operation"][i])
            elif 'close resumed' in close['operation'][i]:
                pid_close_resumed.append(close["pid"][i])
                time_close_resumed.append(close["time"][i])
                operation_close_resumed.append(close["operation"][i])
            else:
                close_counter = close_counter + 1
        print(close_counter)

        closeuf = pd.DataFrame({'pid': pid_close_unfinished, 'time': time_close_unfinished,
                                'operation': operation_close_unfinished})
        closeres = pd.DataFrame({'pid': pid_close_resumed, 'time': time_close_resumed,
                                 'operation': operation_close_resumed})

        # close["operation"].str.contains('close').value_counts()
        # close["operation"].str.contains('unfinished').value_counts()
        # close["operation"].str.contains('close resumed').value_counts()

        new = closeuf["operation"].str.split("(", n=1, expand=True)
        closeuf["operation"] = new[0]
        closeuf["idfile"] = new[1]
        closeuf.tail()

        closeuf["idfile"] = closeuf["idfile"].str.lstrip(' ')
        closeuf["idfile"] = closeuf["idfile"].str.replace('<unfinished', '').str.replace('.', '')
        closeuf["idfile"] = closeuf["idfile"].str.replace('>', '')
        # closeuf.to_excel('closeuf.xlsx', index=False, engine='xlsxwriter')

        new = closeres["operation"].str.split('>', n=1, expand=True)
        closeres["operation"] = new[0]
        closeres["size"] = new[1]
        closeres["operation"] = closeres["operation"].str.replace('<', '').str.replace('.', '')
        closeres["operation"] = closeres["operation"].str.replace('resumed', '')
        closeres["operation"] = closeres["operation"].str.lstrip(' ')
        closeres["size"] = closeres["size"].str.replace(')', '').str.replace('=', '')
        closeres["size"] = closeres["size"].str.lstrip(' ')
        # closeres.to_excel('closeres.xlsx', index=False, engine='xlsxwriter')

        closemixed = closeres.combine_first(closeuf)  # combine_first() fuction for closemixed.

        closemixed.to_excel('closemixed.xlsx', index=False, engine='xlsxwriter')

        # ---------------------------------- CLOSEPURE -------------------------------------
        pid_pure_close = list()
        time_pure_close = list()
        operation_pure_close = list()

        unwanted_counter = 0
        for i in range(0, len(close)):
            if 'unfinished' not in close["operation"][i] and 'resumed' not in close["operation"][i]:
                pid_pure_close.append(close["pid"][i])
                time_pure_close.append(close["time"][i])
                operation_pure_close.append(close["operation"][i])
            else:
                unwanted_counter = unwanted_counter + 1
        print(unwanted_counter)

        closepure = pd.DataFrame({'pid': pid_pure_close, 'time': time_pure_close,
                                  'operation': operation_pure_close})

        closepure.to_excel('closepure.xlsx', index=False, engine='xlsxwriter')

        # Changing the dataframe from close to closepure..
        new = closepure["operation"].str.split("(", n=1, expand=True)
        closepure["operation"] = new[0]
        closepure["idfile"] = new[1]
        new = closepure["idfile"].str.split('=', n=1, expand=True)
        closepure["idfile"] = new[0]
        closepure["size"] = new[1]
        closepure["idfile"] = closepure["idfile"].str.replace(')', '')
        closepure["size"] = closepure["size"].str.lstrip(' ')
        new = closepure["size"].str.split(" ", n=1, expand=True)
        closepure["size"] = new[0]
        closepure["error"] = new[1]
        closepure.to_excel('closepure.xlsx', index=False, engine='xlsxwriter')

        closepure = closepure[['pid', 'time', 'operation', 'idfile', 'size', 'error']]
        closemixed = closemixed[['pid', 'time', 'operation', 'idfile', 'size']]

        closepure.to_excel('closepure.xlsx', index=False, engine='xlsxwriter')
        closemixed.to_excel('closemixed.xlsx', index=False, engine='xlsxwriter')

        # Concatenating with closemixed and closepure to make just one excel file from them called as close.xlsx
        # This file(close.xlsx) will keep inside ./output/data folder.
        close = pd.concat([closemixed, closepure], sort=False)

        close["operation"].str.contains('close').value_counts()

        os.chdir("/Users/ylmrdm/mlio/data/interim")

        close.to_excel('close.xlsx', index=False, engine='xlsxwriter')

        print("Number of write operations; \n", len(write))
        print("Number of read operations; \n", len(read))
        print("Number of open operations; \n", len(open))
        print("Number of close operations; \n", len(close))

    def combiner():
        """
        Combiner Function.
        """
        os.chdir("/Users/ylmrdm/mlio/data/interim")

        extension = 'xlsx'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        print(all_filenames)

        df = pd.concat([pd.read_excel(f) for f in all_filenames], sort=False)

        os.chdir("/Users/ylmrdm/mlio/data/preprocessed")

        df.to_excel("df.xlsx", index=False, encoding='utf-8-sig')

        # There are 5 unfinished read operations and they did not correspond w/ resumed operations.
        # len(readuf)
        # len(readres)

        print("Total No of Write: \n", df["operation"].str.contains('write').value_counts())

    def modeler():
        """
        Modeler Function.
        """
        os.chdir("/Users/ylmrdm/mlio/data/preprocessed")

        df_file = 'df.xlsx'

        # Defining the sheet from df.xlsx
        df_xlsx = pd.ExcelFile(df_file)
        print(type(df_xlsx))
        df_sheets = []
        for sheet in df_xlsx.sheet_names:
            df_sheets.append(df_xlsx.parse(sheet))
        df_sheets = pd.read_excel(df_file, sheet_name=None, header=None, skiprows=1)
        df = pd.concat(df_sheets, sort=False)

        df.columns = ['pid', 'time', 'operation', 'path', 'idfile', 'rs', 'size', 'error', 'flag']

        df.head()

        df[['error_label']] = df[['error']].applymap(lambda x: 0 if pd.isnull(x) else 1)
        df['operation'] = df['operation'].str.replace(' ', '')
        labelencoder = LabelEncoder()
        df['operation_label'] = labelencoder.fit_transform(df['operation'])
        len(df['operation_label'])
        df['operation_label'].head()
        df.to_excel("df.xlsx", index=False, encoding='utf-8-sig')

        # Just a check
        df['error_label'][3164] + df['error_label'][2771]

        df = df[['pid', 'time', 'operation', 'operation_label', 'path', 'idfile',
                 'rs', 'size', 'error', 'error_label', 'flag']]

        df.to_excel("df.xlsx", index=False, encoding='utf-8-sig')
        df.to_csv('data.csv', encoding='utf-8', index=False)
        df.to_excel('data.xlsx', index=False, encoding='utf-8-sig')

        data = pd.read_csv("data.csv")
        data.head()
        sns.FacetGrid(data, hue="error_label", height=5).map(sns.distplot, "operation_label").add_legend()
        data.dtypes
        # sns.pairplot(data, vars=['pid', 'rs', 'error_label'], hue='operation')

if __name__ == '__main__':
    PsCm.parser()
    PsCm.separator()
    PsCm.combiner()
    PsCm.modeler()

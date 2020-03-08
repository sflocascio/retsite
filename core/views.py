from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from core.models import  Document, Process, Ret, Process
from django.contrib import messages
import csv
import json
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from core.forms import *
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from core.utils import *
#from core.forms import FileForm

def index(request):
    refs = Process.objects.prefetch_related('process').order_by('-created_date')
    files = Document.objects.prefetch_related('process').all()
    rets = Ret.objects.select_related('parent_ref_number').all()
    # docs = Document.objects.get(process__exact = files.ref_number)
    
    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in %r: %s" % (cwd, files))
   
    return render(request, 'index.html', {
        'refs'  : refs,
        'rets'  : rets,
        'files'  : files,
    })

def session_table(request, pk):
    # refs = Process.objects.get('process').all()
    # files = Document.objects.prefetch_related('process').all()
    # rets = Ret.objects.select_related('parent_ref_number').all()
    refs = Process.objects.get(pk=pk)
    docs = refs.process.all()
    rets = refs.parent_ref_number.all()
    alpha_pos_4 = rets.filter(sector_id__contains='ALPHA POS 4')
    gamma_pos_2 = rets.filter(sector_id__contains='GAMMA POS 2')
    beta_pos_2 = rets.filter(sector_id__contains='BETA POS 2')
    #BETA POS 2
    #Entry.objects.get(headline__contains='Lennon')
   
    return render(request, 'session_table.html', {
        'refs'  : refs,
        'docs'  : docs,
        'rets'  : rets,
        'alpha_pos_4' : alpha_pos_4,
        'gamma_pos_2' : gamma_pos_2,
        'beta_pos_2' : beta_pos_2,
    })

def session_detail(request, pk):
    # refs = Process.objects.get('process').all()
    # files = Document.objects.prefetch_related('process').all()
    # rets = Ret.objects.select_related('parent_ref_number').all()
    refs = Process.objects.get(pk=pk)
    docs = refs.process.all()
    rets = refs.parent_ref_number.all()
    alpha_pos_4 = rets.filter(sector_id__contains='ALPHA POS 4')
    gamma_pos_2 = rets.filter(sector_id__contains='GAMMA POS 2')
    #Entry.objects.get(headline__contains='Lennon')
   
    return render(request, 'session_detail.html', {
        'refs'  : refs,
        'docs'  : docs,
        'rets'  : rets,
        'alpha_pos_4' : alpha_pos_4,
        'gamma_pos_2' : gamma_pos_2,
    })

#View of Parent Session Detail
def session_detail_v2(request, pk):
    refs = Process.objects.get(pk=pk)
    docs = refs.process.all()
    process = Process.objects.get(pk=pk)
    rets = refs.parent_ref_number.all()
    technologies = refs.parent_ref_number_tech.all()

    alpha_pos_4 = rets.filter(sector_id__contains='ALPHA POS 4')
    gamma_pos_2 = rets.filter(sector_id__contains='GAMMA POS 2')
    beta_pos_2 = rets.filter(sector_id__contains='BETA POS 2')

    if request.POST.get("sendinfo"):  
            alpha_pos_4.delete()
    if request.POST.get("delete_tech"):  
            technologies.delete()

    form1 = DocumentForm(prefix="a1")
    form2 = DocumentForm(prefix="a2")
    form3 = DocumentForm(prefix="a3")
    form4 = DocumentForm(prefix="a4")
    form5 = DocumentForm(prefix="a5")
    form6 = DocumentForm(prefix="a6")
    form7 = DocumentForm(prefix="a7")
    form8 = DocumentForm(prefix="a8")
    form9 = DocumentForm(prefix="a9")
    form10 = DocumentForm(prefix="a10")
    form11 = DocumentForm(prefix="a11")
    form12 = DocumentForm(prefix="a12")

    modified_file_list = []
    uploaded_file_list = []

    #Handle All Ret FILE Uploads HERE
    if request.method == "POST":
        
        print(" \n === Entered New Upload Block === Method is POST ... ")
        newfile = DocumentForm(request.POST, request.FILES, prefix="a2")
        newfile2 = DocumentForm(request.POST, request.FILES, prefix="a1")
        newfile3 = DocumentForm(request.POST, request.FILES, prefix="a3")
        newfile4 = DocumentForm(request.POST, request.FILES, prefix="a4")
        newfile5 = DocumentForm(request.POST, request.FILES, prefix="a5")
        newfile6 = DocumentForm(request.POST, request.FILES, prefix="a6")
        newfile7 = DocumentForm(request.POST, request.FILES, prefix="a7")
        newfile8 = DocumentForm(request.POST, request.FILES, prefix="a8")
        newfile9 = DocumentForm(request.POST, request.FILES, prefix="a9")
        newfile10 = DocumentForm(request.POST, request.FILES, prefix="a10")
        newfile11 = DocumentForm(request.POST, request.FILES, prefix="a11")
        newfile12 = DocumentForm(request.POST, request.FILES, prefix="a12")
        uploaded_file_list.append(newfile)
        uploaded_file_list.append(newfile2)
        uploaded_file_list.append(newfile3)
        uploaded_file_list.append(newfile4)
        uploaded_file_list.append(newfile5)
        uploaded_file_list.append(newfile6)
        uploaded_file_list.append(newfile7)
        uploaded_file_list.append(newfile8)
        uploaded_file_list.append(newfile9)
        uploaded_file_list.append(newfile10)
        uploaded_file_list.append(newfile11)
        uploaded_file_list.append(newfile12)

        print("UploadedFileList:::: ", uploaded_file_list)
        #session_name = request.POST.get('session')

        #process = Process(session_name = session_name)
        #happy = process.save()

        print("New process REF NUMBER :", process.ref_number)
            #print("This is the Newfile that is created in loop", newfile.document)
            #newfile = Document(document = formfile) #Using model. not Form
        #if newfile.is_valid() or newfile2.is_valid():
        for the_file in uploaded_file_list:
            if the_file.is_valid():
                print("Entering for Loop. current variable", the_file)
                
                print("New process REF NUMBER in loop:", process.ref_number)
                # if not you can only using `obj = form.save()`
                original_file_name = the_file.cleaned_data['document']
                print("Original FILE NAME:", original_file_name)
                if original_file_name != None:
                    #original_file_name2 = newfile2.cleaned_data['document']
                    #initial_obj = the_file.save(commit=False)
                    #print("HELP", initial_obj.document)
                    modified_file_name = the_file.save()
                    modified_file_name.process = process
                    print("THE FILE.PROCESS:", modified_file_name.process)
                    #modified_file_name2 = newfile2.save()
                    updated_file = modified_file_name.save()
                    print("Original File Name", original_file_name)
                    #print("Modified File Name ", modified_file_name.document)
                
                    #print("Document Object saved, from file that was renamed:", newfile)
                    
                    #cleaned_file = newfile
                    #print("CLEANED FILE:", cleaned_file)
                    #cleaned_file = newfile.document
                    #print("cleanedFILE:", cleaned_file.document)
                    modified_file_list.append(modified_file_name.document)
                    #modified_file_list.append(modified_file_name2.document)
                    #print("Current Cleaned FILE LIST", cleaned_file_list)
                    print(" Modified LIST ", modified_file_list)
                    print(" repeating FOR loop ")
                    # print("Inital OBject.document.url:", initial_obj.document.url)
            else:
                print("Form NOT valid")


    else:
        file = DocumentForm()
        print("Entered Else Block of FORM validation")

    print("\n === EXITED upload block ====")
    total_rets_created = 0
    for input_file in modified_file_list:
        uploaded_file_name = Document.objects.get(document = input_file)
        print("Current FILER document name", uploaded_file_name.document)
        #Splits the Input File in individual RET.Txt files 
        with open(uploaded_file_name.document.path) as fo:
            print("entered Parsing Block ")
            op = ''
            start = 0
            cntr = 1
            files_created = []
            for x in fo.read().split("\n"):
                if not x.strip():
                    if(start == 1):
                        with open(str(cntr) + '.txt', 'w') as opf:
                            opf.write(op)
                            name_of_file = opf
                            if (opf.name != '1.txt'):
                                files_created.append(opf.name)
                            print(opf.name)
                            opf.close()
                            op = ''
                            cntr += 1
                    else:
                        start = 1
                else:
                    if (op == ''):
                        op = x
                    else:
                        op = op + '\n' + x
            total_files_created = cntr - 1
            print( "total # of files created" , total_files_created)
            print("Files Created LIST ", files_created)
            fo.close()
        
        # Turn one TXT file into JSON RET object 
        #filename = '4.txt'
        
        jsoncntr = 1
        json_files_created = []
        for filename in files_created:
            commands = {}
            print("JSON cntertop", jsoncntr)
            with open(filename) as fh:
                print(filename)
                for line in fh:
                    command, description = line.strip().split(':', 1)
                    commands[command] = description.strip()

            # dump into JSON File 
            with open(str(jsoncntr) + '.json', 'w') as fp:
                json_files_created.append(fp.name)
                fp.write("{" + "\n" + '"' + "Data"+ '":['  )
                json.dump(commands, fp, indent=2, sort_keys=True)
                fp.write("\n" + "]" + "\n" + "}" )
                jsoncntr += 1
                total_rets_created += 1
                print("JSON COunter bottom:", jsoncntr)

        for file in json_files_created:
            print("Entering Creating Objects BLOCK ")
            print("file in process block:", file)
            # Read file 
            f = open(file)
            json_string = f.read()
            f.close()
            data = json.loads(json_string)
            #Add variables and parsing for band, technology, operating_band

            for values in data['Data']:
                station_id = values['Station ID']

                print("StationID HERE::", station_id)
                position_code = get_sector_and_position_code(station_id)
                band = get_band(station_id)
                technology = get_technology(station_id)
                operating_band = get_operating_band(band, technology)

                #Handle Technologies that Come back empty and set subunit if they are, otherwise set to undefined
                if operating_band == '--':
                    ret_sub_unit = station_id
                else:
                    ret_sub_unit = 'not yet defined'
                #get or update tecnology object here 
                update_or_create_technology_object(operating_band, process)

                #print('RET position after function here:::', ret_position)

                #RET object created here 
                object = Ret.objects.create(
                ret_position = get_ret_position(position_code),
                band = band, #set above
                operating_band = operating_band, #set above
                ret_sub_unit = ret_sub_unit,
                technology = technology, #set above 
                parent_ref_number = process, #set to parent ref 
                address=values['Address'],
                ret_name=file , 
                aisg_version=values['AISG Version'], 
                bearing=values['Bearing'],
                station_id=values['Station ID'], 
                sector_id=values['Sector ID'], 
                hw_version=values['HW Version'])
                print("object ADdress: ", object.address)
                object.save()
            print("JSON file list created:", json_files_created)

  
    messages.success(request,  "Rets Detected: {} ".format(total_rets_created))

    print("TOTAL REST CREATED", total_rets_created)
    total_rets_created = 0
    print("TOTAL REST CREATED after 0", total_rets_created)

    

   
    return render(request, 'session_detail_v2.html', {
        'refs'  : refs,
        'docs'  : docs,
        'rets'  : rets,
        'technologies'  : technologies,
        'alpha_pos_4' : alpha_pos_4,
        'gamma_pos_2' : gamma_pos_2,
        'beta_pos_2' : beta_pos_2,
        'form1'  : form1 ,
        'form2'  : form2 ,
        'form3'  : form3 ,
        'form4'  : form4 ,
        'form5'  : form5 ,
        'form6'  : form6 ,
        'form7'  : form7 ,
        'form8'  : form8 ,
        'form9'  : form9 ,
        'form10'  : form10 ,
        'form11'  : form11 ,
        'form12'  : form12 ,
    })
      
def process(request):
    #towers = Tower.objects.all()
    now = timezone.now()
    form1 = DocumentForm(prefix="a1")
    form2 = DocumentForm(prefix="a2")
    form3 = DocumentForm(prefix="a3")
    form4 = DocumentForm(prefix="a4")
    form5 = DocumentForm(prefix="a5")
    form6 = DocumentForm(prefix="a6")
    form7 = DocumentForm(prefix="a7")
    form8 = DocumentForm(prefix="a8")
    form9 = DocumentForm(prefix="a9")
    form10 = DocumentForm(prefix="a10")
    form11 = DocumentForm(prefix="a11")
    form12 = DocumentForm(prefix="a12")
    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in %r: %s" % (cwd, files))
    return render(request, 'about.html', {
        
        'form1'  : form1 ,
        'form2'  : form2 ,
        'form3'  : form3 ,
        'form4'  : form4 ,
        'form5'  : form5 ,
        'form6'  : form6 ,
        'form7'  : form7 ,
        'form8'  : form8 ,
        'form9'  : form9 ,
        'form10'  : form10 ,
        'form11'  : form11 ,
        'form12'  : form12 ,
        'now' : now,
    })    

#View for Creating Parent Session
def process_v2(request):
    now = timezone.now()

    return render(request, 'process_v2.html', {
        'now' : now,
    })

#Generates Parent Session 
def create_session_form(request, *args, **kwargs):
    #Using ModelForm to create OBJECTS
    #file_upload = '/Users/samsmacbookair/projects/john_proj/core/retStaged.txtrpt'
    if request.method == "POST":
        print(" \n === Entered New Upload Block === Method is POST ... ")

        fcc_id = request.POST.get('fcc_id')
        site_common_name = request.POST.get('site_common_name')
        market = request.POST.get('market')
        enode_b_id = request.POST.get('enode_b_id')
        ptn = request.POST.get('ptn')
        release = request.POST.get('release')

        process = Process(fcc_id = fcc_id, 
        site_common_name = site_common_name,
        market = market,
        enode_b_id = enode_b_id,
        ptn = ptn, 
        release =release
        )
        happy = process.save()

    else:
        print("Invalied")
        
    messages.success(request, "Session Created: '{}' ".format(process.fcc_id))
    return redirect('home')

#Original version of Parent + Ret object creation
def create_object_form(request, pk, *args, **kwargs):
    #Using ModelForm to create OBJECTS
    #file_upload = '/Users/samsmacbookair/projects/john_proj/core/retStaged.txtrpt'
    if request.method == "POST":
        
        print(" \n === Entered New Upload Block === Method is POST ... ")
        #print("Input List", input_list)
        #file = DocumentForm(request.POST, request.FILES)
        modified_file_list = []
        uploaded_file_list = []

        newfile = DocumentForm(request.POST, request.FILES, prefix="a2")
        newfile2 = DocumentForm(request.POST, request.FILES, prefix="a1")
        newfile3 = DocumentForm(request.POST, request.FILES, prefix="a3")
        newfile4 = DocumentForm(request.POST, request.FILES, prefix="a4")
        newfile5 = DocumentForm(request.POST, request.FILES, prefix="a5")
        newfile6 = DocumentForm(request.POST, request.FILES, prefix="a6")
        newfile7 = DocumentForm(request.POST, request.FILES, prefix="a7")
        newfile8 = DocumentForm(request.POST, request.FILES, prefix="a8")
        newfile9 = DocumentForm(request.POST, request.FILES, prefix="a9")
        newfile10 = DocumentForm(request.POST, request.FILES, prefix="a10")
        newfile11 = DocumentForm(request.POST, request.FILES, prefix="a11")
        newfile12 = DocumentForm(request.POST, request.FILES, prefix="a12")
        uploaded_file_list.append(newfile)
        uploaded_file_list.append(newfile2)
        uploaded_file_list.append(newfile3)
        uploaded_file_list.append(newfile4)
        uploaded_file_list.append(newfile5)
        uploaded_file_list.append(newfile6)
        uploaded_file_list.append(newfile7)
        uploaded_file_list.append(newfile8)
        uploaded_file_list.append(newfile9)
        uploaded_file_list.append(newfile10)
        uploaded_file_list.append(newfile11)
        uploaded_file_list.append(newfile12)

        print("UploadedFileList:::: ", uploaded_file_list)
        session_name = request.POST.get('session')

        process = Process(session_name = session_name)
        happy = process.save()

        print("New process REF NUMBER :", process.ref_number)
            #print("This is the Newfile that is created in loop", newfile.document)
            #newfile = Document(document = formfile) #Using model. not Form
        #if newfile.is_valid() or newfile2.is_valid():
        for the_file in uploaded_file_list:
            if the_file.is_valid():
                print("Entering for Loop. current variable", the_file)
                
                print("New process REF NUMBER in loop:", process.ref_number)
                # if not you can only using `obj = form.save()`
                original_file_name = the_file.cleaned_data['document']
                print("Original FILE NAME:", original_file_name)
                if original_file_name != None:
                    #original_file_name2 = newfile2.cleaned_data['document']
                    #initial_obj = the_file.save(commit=False)
                    #print("HELP", initial_obj.document)
                    modified_file_name = the_file.save()
                    modified_file_name.process = process
                    print("THE FILE.PROCESS:", modified_file_name.process)
                    #modified_file_name2 = newfile2.save()
                    updated_file = modified_file_name.save()
                    print("Original File Name", original_file_name)
                    #print("Modified File Name ", modified_file_name.document)
                
                    #print("Document Object saved, from file that was renamed:", newfile)
                    
                    #cleaned_file = newfile
                    #print("CLEANED FILE:", cleaned_file)
                    #cleaned_file = newfile.document
                    #print("cleanedFILE:", cleaned_file.document)
                    modified_file_list.append(modified_file_name.document)
                    #modified_file_list.append(modified_file_name2.document)
                    #print("Current Cleaned FILE LIST", cleaned_file_list)
                    print(" Modified LIST ", modified_file_list)
                    print(" repeating FOR loop ")
                    # print("Inital OBject.document.url:", initial_obj.document.url)
            else:
                print("Form NOT valid")


    else:
        file = DocumentForm()
        print("Entered Else Block of FORM validation")

    print("\n === EXITED upload block ====")
    total_rets_created = 0
    for input_file in modified_file_list:
        uploaded_file_name = Document.objects.get(document = input_file)
        print("Current FILER document name", uploaded_file_name.document)
        #Splits the Input File in individual RET.Txt files 
        with open(uploaded_file_name.document.path) as fo:
            print("entered Parsing Block ")
            op = ''
            start = 0
            cntr = 1
            files_created = []
            for x in fo.read().split("\n"):
                if not x.strip():
                    if(start == 1):
                        with open(str(cntr) + '.txt', 'w') as opf:
                            opf.write(op)
                            name_of_file = opf
                            if (opf.name != '1.txt'):
                                files_created.append(opf.name)
                            print(opf.name)
                            opf.close()
                            op = ''
                            cntr += 1
                    else:
                        start = 1
                else:
                    if (op == ''):
                        op = x
                    else:
                        op = op + '\n' + x
            total_files_created = cntr - 1
            print( "total # of files created" , total_files_created)
            print("Files Created LIST ", files_created)
            fo.close()
        
        # Turn one TXT file into JSON RET object 
        #filename = '4.txt'
        
        jsoncntr = 1
        json_files_created = []
        for filename in files_created:
            commands = {}
            print("JSON cntertop", jsoncntr)
            with open(filename) as fh:
                print(filename)
                for line in fh:
                    command, description = line.strip().split(':', 1)
                    commands[command] = description.strip()

            # dump into JSON File 
            with open(str(jsoncntr) + '.json', 'w') as fp:
                json_files_created.append(fp.name)
                fp.write("{" + "\n" + '"' + "Data"+ '":['  )
                json.dump(commands, fp, indent=2, sort_keys=True)
                fp.write("\n" + "]" + "\n" + "}" )
                jsoncntr += 1
                total_rets_created += 1
                print("JSON COunter bottom:", jsoncntr)

        for file in json_files_created:
            print("Entering Creating Objects BLOCK ")
            print("file in process block:", file)
            # Read file 
            f = open(file)
            json_string = f.read()
            f.close()
            data = json.loads(json_string)
            #Add variables and parsing for band, technology, operating_band

            for values in data['Data']:
                object = Ret.objects.create(
                parent_ref_number = process,
                address=values['Address'],
                ret_name=file , 
                aisg_version=values['AISG Version'], 
                bearing=values['Bearing'],
                station_id=values['Station ID'], 
                sector_id=values['Sector ID'], 
                hw_version=values['HW Version'])
                print("object ADdress: ", object.address)
                object.save()
            print("JSON file list created:", json_files_created)

    messages.success(request, "Session Created: '{}' ".format(process.session_name))
    messages.success(request,  "Rets Detected: {} ".format(total_rets_created))

    print("TOTAL REST CREATED", total_rets_created)
    total_rets_created = 0
    print("TOTAL REST CREATED after 0", total_rets_created)
    print("SESSION NAME:" , process.session_name )
    return redirect('home')
    #return render(request, 'index.html')

#New version of independent Antenna Uploads
def process_antenna_file(request, *args, **kwargs):
    #Using ModelForm to create OBJECTS
    #Saved off of create_object_form - New version that doesnt create them all at the same time 
    process = Process.objects.get(pk=pk)
    
    if request.method == "POST":
        
        print(" \n === Entered New Upload Block === Method is POST ... ")
        #print("Input List", input_list)
        #file = DocumentForm(request.POST, request.FILES)
        modified_file_list = []
        uploaded_file_list = []

        newfile = DocumentForm(request.POST, request.FILES, prefix="a2")
        newfile2 = DocumentForm(request.POST, request.FILES, prefix="a1")
        newfile3 = DocumentForm(request.POST, request.FILES, prefix="a3")
        newfile4 = DocumentForm(request.POST, request.FILES, prefix="a4")
        newfile5 = DocumentForm(request.POST, request.FILES, prefix="a5")
        newfile6 = DocumentForm(request.POST, request.FILES, prefix="a6")
        newfile7 = DocumentForm(request.POST, request.FILES, prefix="a7")
        newfile8 = DocumentForm(request.POST, request.FILES, prefix="a8")
        newfile9 = DocumentForm(request.POST, request.FILES, prefix="a9")
        newfile10 = DocumentForm(request.POST, request.FILES, prefix="a10")
        newfile11 = DocumentForm(request.POST, request.FILES, prefix="a11")
        newfile12 = DocumentForm(request.POST, request.FILES, prefix="a12")
        uploaded_file_list.append(newfile)
        uploaded_file_list.append(newfile2)
        uploaded_file_list.append(newfile3)
        uploaded_file_list.append(newfile4)
        uploaded_file_list.append(newfile5)
        uploaded_file_list.append(newfile6)
        uploaded_file_list.append(newfile7)
        uploaded_file_list.append(newfile8)
        uploaded_file_list.append(newfile9)
        uploaded_file_list.append(newfile10)
        uploaded_file_list.append(newfile11)
        uploaded_file_list.append(newfile12)

        print("UploadedFileList:::: ", uploaded_file_list)
        #session_name = request.POST.get('session')

        #process = Process(session_name = session_name)
        #happy = process.save()

        print("New process REF NUMBER :", process.ref_number)
            #print("This is the Newfile that is created in loop", newfile.document)
            #newfile = Document(document = formfile) #Using model. not Form
        #if newfile.is_valid() or newfile2.is_valid():
        for the_file in uploaded_file_list:
            if the_file.is_valid():
                print("Entering for Loop. current variable", the_file)
                
                print("New process REF NUMBER in loop:", process.ref_number)
                # if not you can only using `obj = form.save()`
                original_file_name = the_file.cleaned_data['document']
                print("Original FILE NAME:", original_file_name)
                if original_file_name != None:
                    #original_file_name2 = newfile2.cleaned_data['document']
                    #initial_obj = the_file.save(commit=False)
                    #print("HELP", initial_obj.document)
                    modified_file_name = the_file.save()
                    modified_file_name.process = process
                    print("THE FILE.PROCESS:", modified_file_name.process)
                    #modified_file_name2 = newfile2.save()
                    updated_file = modified_file_name.save()
                    print("Original File Name", original_file_name)
                    #print("Modified File Name ", modified_file_name.document)
                
                    #print("Document Object saved, from file that was renamed:", newfile)
                    
                    #cleaned_file = newfile
                    #print("CLEANED FILE:", cleaned_file)
                    #cleaned_file = newfile.document
                    #print("cleanedFILE:", cleaned_file.document)
                    modified_file_list.append(modified_file_name.document)
                    #modified_file_list.append(modified_file_name2.document)
                    #print("Current Cleaned FILE LIST", cleaned_file_list)
                    print(" Modified LIST ", modified_file_list)
                    print(" repeating FOR loop ")
                    # print("Inital OBject.document.url:", initial_obj.document.url)
            else:
                print("Form NOT valid")


    else:
        file = DocumentForm()
        print("Entered Else Block of FORM validation")

    print("\n === EXITED upload block ====")
    total_rets_created = 0
    for input_file in modified_file_list:
        uploaded_file_name = Document.objects.get(document = input_file)
        print("Current FILER document name", uploaded_file_name.document)
        #Splits the Input File in individual RET.Txt files 
        with open(uploaded_file_name.document.path) as fo:
            print("entered Parsing Block ")
            op = ''
            start = 0
            cntr = 1
            files_created = []
            for x in fo.read().split("\n"):
                if not x.strip():
                    if(start == 1):
                        with open(str(cntr) + '.txt', 'w') as opf:
                            opf.write(op)
                            name_of_file = opf
                            if (opf.name != '1.txt'):
                                files_created.append(opf.name)
                            print(opf.name)
                            opf.close()
                            op = ''
                            cntr += 1
                    else:
                        start = 1
                else:
                    if (op == ''):
                        op = x
                    else:
                        op = op + '\n' + x
            total_files_created = cntr - 1
            print( "total # of files created" , total_files_created)
            print("Files Created LIST ", files_created)
            fo.close()
        
        # Turn one TXT file into JSON RET object 
        #filename = '4.txt'
        
        jsoncntr = 1
        json_files_created = []
        for filename in files_created:
            commands = {}
            print("JSON cntertop", jsoncntr)
            with open(filename) as fh:
                print(filename)
                for line in fh:
                    command, description = line.strip().split(':', 1)
                    commands[command] = description.strip()

            # dump into JSON File 
            with open(str(jsoncntr) + '.json', 'w') as fp:
                json_files_created.append(fp.name)
                fp.write("{" + "\n" + '"' + "Data"+ '":['  )
                json.dump(commands, fp, indent=2, sort_keys=True)
                fp.write("\n" + "]" + "\n" + "}" )
                jsoncntr += 1
                total_rets_created += 1
                print("JSON COunter bottom:", jsoncntr)

        for file in json_files_created:
            print("Entering Creating Objects BLOCK ")
            print("file in process block:", file)
            # Read file 
            f = open(file)
            json_string = f.read()
            f.close()
            data = json.loads(json_string)
            #Add variables and parsing for band, technology, operating_band

            for values in data['Data']:
                object = Ret.objects.create(
                parent_ref_number = process,
                address=values['Address'],
                ret_name=file , 
                aisg_version=values['AISG Version'], 
                bearing=values['Bearing'],
                station_id=values['Station ID'], 
                sector_id=values['Sector ID'], 
                hw_version=values['HW Version'])
                print("object ADdress: ", object.address)
                object.save()
            print("JSON file list created:", json_files_created)

    messages.success(request, "Session Created: '{}' ".format(process.session_name))
    messages.success(request,  "Rets Detected: {} ".format(total_rets_created))

    print("TOTAL REST CREATED", total_rets_created)
    total_rets_created = 0
    print("TOTAL REST CREATED after 0", total_rets_created)
    print("SESSION NAME:" , process.session_name )
    return redirect('home')
    #return render(request, 'index.html')

#Exports CSV file
def export_csv(request, pk):
    refs = Process.objects.get(pk=pk)
    docs = refs.process.all()
    rets = refs.parent_ref_number.all()
    alpha_pos_4 = rets.filter(sector_id__contains='ALPHA POS 4')
    gamma_pos_2 = rets.filter(sector_id__contains='GAMMA POS 2')
    beta_pos_2 = rets.filter(sector_id__contains='BETA POS 2')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attatchment; filename="export.csv"'
    writer = csv.writer(response, delimiter=",")
    writer.writerow(['SectorID', 'Address', 'StationID', 'HW Version', 'Bearing', 'AISG Version', 'RetName'])

    for a in gamma_pos_2:
        writer.writerow([a.sector_id, a.address, a.station_id, a.hw_version, a.bearing, a.aisg_version, a.ret_name])
    writer.writerow([" "])
    writer.writerow(["Hello"])
    for a in gamma_pos_2:
        writer.writerow([a.sector_id, a.address, a.station_id, a.hw_version, a.bearing, a.aisg_version, a.ret_name])
    return(response)


def update_technology_cell_id(request, pk):
    refs = Technology.objects.get(pk=pk)
    session_id = refs.parent_ref_number.id
    form_class = TechnologyForm
    parent_session = refs.parent_ref_number
    rets = parent_session.parent_ref_number.all()
    session = refs.parent_ref_number
    #rets = refs.parent_ref_number.all()

    if request.method =='POST':
        form = form_class(data=request.POST, instance=refs)
        if form.is_valid():
            technology_operating_band = form.cleaned_data['technology_operating_band']
            technology_cell_id = form.cleaned_data['technology_cell_id']
            form.save()
            for ret in rets:
                if ret.operating_band == technology_operating_band:
                    ret.ret_cell_id = technology_cell_id
                    #Here you have the indv. ret and it's attributes for play 
                    prefix = get_eutran_prefix(ret.station_id) #returns A,B, or C 
                    ret.eutran_cell_id = set_eutran_cell_id(ret.band, ret.ret_cell_id, prefix)
                    ret.ret_sub_unit = set_ret_sub_unit(ret.station_id, ret.eutran_cell_id)
                    ret.save()
                    

            # return redirect('home')
            return redirect('session_detail_v2', pk=session_id)
    else:
        form = form_class(instance=refs)
    return render(request, 'edit_technology.html', {'refs': refs, 'form': form, 'session': session,})


def delete_all_files(request, pk):
    refs = Process.objects.get(pk=pk)
    print("entered DELETE All files")
    # session_id = refs.id
    refs.delete()
    # docs = refs.process.all()
    # process = Process.objects.get(pk=pk)
    # rets = parent_session.parent_ref_number.all()
    # technologies = Technology.objects.get(pk=pk)


    # card = Document.objects.get(pk=pk)
    # quiz_id = card.quiz.id
    # if (request.user == quiz.author) or (request.user.is_staff):
    # for d in docs:
    #     print("docs ptined:", d.document)
    #     d.delete()
    # for t in technologies:
    #     t.delete()
    # for r in rets:
    #     r.delete()

    #messages.success(request, f'Card "{card.answer}" Deleted')
    #return redirect('session_detail_v2', pk=session_id)
    return redirect('home')
    # return render(request, 'quizzes/quiz_detail.html',)







# if method == POST:
#     technology = Something to get the specific technology 
#       Need to set the Foreign Keys to each otheer 
#     technology_cell_id = user input on this specfic form 
#     technolgy_cell_id.save()

#     for ret in rets:
#         if ret.operating_band == tecnology.operating_band:
#             ret.cell_id = technology_cell_id 
#             ret.save() or update   
#         else: 
#             pass


#     refs = Process.objects.get(pk=pk)
#     docs = refs.process.all()
#     process = Process.objects.get(pk=pk)
#     rets = refs.parent_ref_number.all()
#     technologies = refs.parent_ref_number_tech.all()
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


def index(request):
    return render(request, 'index.html')

def quiz(request):
    return render(request, 'quiz.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


def quiz(request):
    return render(request, 'quiz.html')


import json
import requests
from google.cloud import speech_v1p1beta1 as speech
import os
import boto3
import json

#--------------MOM FUNCTION FROM BELOW----------------------------------


def therapy_report_fn(transcription):
    prompt_data=""" You are a proficient AI with a specialty in finding the following topic from transcript
    Annalise the give transcribe of therapy session in detail as expert psychologist Please provide a comprehensive assessment for a client, including potential diagnoses based on the DSM-5-TR version in table format, a structured risk assessment table detailing the client's suicide risk level, intent to act, plan to act, means to act, and any identified protective factors, medications history including medication name, dosage, frequency, start date, and end date, as well as interventions used for the client's treatment.
    Give the result in bullet points and dont repeat anything , be prise to result and use language that human can understand.
    """
    # Concatenate the transcription with the prompt_data
    prompt = "[INST]" + prompt_data + transcription + "[/INST]"

    bedrock = boto3.client(service_name="bedrock-runtime")
    payload = {
        "prompt": prompt,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    model_id = "mistral.mixtral-8x7b-instruct-v0:1"
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get("body").read())
    # print("Result from fn1",response_body)
    return response_body


def therapy_session_fn(transcription):
    prompt_data=""" You are a proficient AI with a specialty in finding the following topic from transcript
Annalise the give transcribe of therapy session in detail as expert psychologist and give 
Summary: Provide a concise overview of the session, focusing on medication, depression, and self-sabotage.
Client Details: Highlight important client background, including medical history and therapy experiences.
Request: Analyse client perspectives, concerns, and therapy goals expressed during the session.
Conclusions: Summarise client insights and action plans.
Interventions: Identify effective therapeutic approaches and significant client responses.
Future Paths: Propose potential directions for future therapy sessions
Give the result in bullet points and dont repeat anything , be prise to result and use language that human can understand.
"""

    # Concatenate the transcription with the prompt_data
    prompt = "[INST]" + prompt_data + transcription + "[/INST]"

    bedrock = boto3.client(service_name="bedrock-runtime")
    payload = {
        "prompt": prompt,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    model_id = "mistral.mixtral-8x7b-instruct-v0:1"
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get("body").read())
    # print("Result from fn2",response_body)
    return response_body

def compre_fn(transcription):
    prompt_data=""" You are a proficient AI with a specialty in finding the following topic from transcript
    Focus on the following aspects:
Client's main concerns
Emotional expression
Communication style
Relationship patterns
Self-reflection
Empathy and connection
Coping mechanisms
Recognition of goals
Conceptualization of success
Patterns of thought
Exploration of past experiences
Client feedback on therapy
Provide insights on each aspect.
Highlight key observations and areas for therapeutic intervention.
Give the result in bullet points and dont repeat anything , be prise to result and use language that human can understand.
    """
    # Concatenate the transcription with the prompt_data
    prompt = "[INST]" + prompt_data + transcription + "[/INST]"

    bedrock = boto3.client(service_name="bedrock-runtime")
    payload = {
        "prompt": prompt,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    model_id = "mistral.mixtral-8x7b-instruct-v0:1"
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get("body").read())
    # print("Result from fn3",response_body)
    return response_body


def blueprint_fn(transcription):
    prompt_data="""Please analyse the transcribed therapy session as an expert psychologist and generate a detailed blueprint for the next therapy session based on the transcript. The blueprint should help in understanding the client's problems better and planning further sessions effectively. Ensure the blueprint includes elements such as session introduction, progress review, therapeutic goals assessment, exploration of current emotional state, goal refinement or expansion, proposed interventions and strategies, homework review, client reflection, discussion of anticipated challenges, empathy and validation, and session closing with homework assignments. Provide this analysis based on the transcript to facilitate targeted therapeutic interventions
Give the result in bullet points and dont repeat anything , be prise to result and use language that human can understand.

    """
    # Concatenate the transcription with the prompt_data
    prompt = "[INST]" + prompt_data + transcription + "[/INST]"

    bedrock = boto3.client(service_name="bedrock-runtime")
    payload = {
        "prompt": prompt,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    model_id = "mistral.mixtral-8x7b-instruct-v0:1"
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get("body").read())
    # print("Result from fn4",response_body)
    return response_body



def goal_fn(transcription):
    prompt_data=""" Please analyse the transcribed therapy session as an expert psychologist and generate homework or a worksheet for the patient to complete before the next session. Tailor the assignment to address the patient's specific issues identified during the session, ensuring it supports their therapeutic goals and encourages reflection and growth. Provide detailed instructions and exercises that are relevant to the client's challenges and conducive to their progress in therapy
    Give the result in bullet points and dont repeat anything , be prise to result and use language that human can understand.
    """
    # Concatenate the transcription with the prompt_data
    prompt = "[INST]" + prompt_data + transcription + "[/INST]"

    bedrock = boto3.client(service_name="bedrock-runtime")
    payload = {
        "prompt": prompt,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    model_id = "mistral.mixtral-8x7b-instruct-v0:1"
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get("body").read())
    # print("Result from fn4",response_body)
    return response_body



def feedback_fn(transcription):
    prompt_data=""" You are a proficient AI with a specialty in finding the following topic from transcript
    Please analyse the transcribed therapy session as an expert psychologist and provide feedback on the therapist's performance. Highlight any mistakes made during the session, areas for improvement, and suggestions for enhancing therapeutic effectiveness. Evaluate the therapist's communication skills, empathy, rapport-building, intervention effectiveness, and overall therapeutic approach. Offer insights on how the therapist can better address the client's needs, improve session structure, and strengthen therapeutic alliance for future sessions
    Give the result in bullet points and dont repeat anything , be prise to result and use language that human can understand.
    """
    # Concatenate the transcription with the prompt_data
    prompt = "[INST]" + prompt_data + transcription + "[/INST]"

    bedrock = boto3.client(service_name="bedrock-runtime")
    payload = {
        "prompt": prompt,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    model_id = "mistral.mixtral-8x7b-instruct-v0:1"
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get("body").read())
    # print("Result from fn4",response_body)
    return response_body


# def meeting_minutes(transcription):
#     therapy_report = therapy_report_fn(transcription)
#     therapy_session = therapy_session_fn(transcription)
#     comprehension_report = compre_fn(transcription)
#     next_session_blueprint = blueprint_fn(transcription)
#     goal=goal_fn(transcription)
#     feedback=feedback_fn(transcription)
#     return {
#         'therapy_report': therapy_report,
#         'therapy_session': therapy_session,
#         'comprehension_report': comprehension_report,
#         'next_session_blueprint': next_session_blueprint,
#         'goal ':goal,
#         'feedback':feedback
#     }


import os
from django.shortcuts import render
from django.http import JsonResponse
from .forms import AudioUploadForm
from .models import MeetingTranscript
import requests
from datetime import datetime

def transcribe_audio(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        try:
            form = AudioUploadForm(request.POST, request.FILES)
            if form.is_valid():
                audio_file = request.FILES['audio_file']
                # Your LemonFox API endpoint
                url = "https://api.lemonfox.ai/v1/audio/transcriptions"
                headers = {"Authorization": "Bearer qSmQFnHz2NuiyjFkaULMQ668VWmJEIS6"}
                data = {"language": "english", "response_format": "json"}
                files = {"file": (audio_file.name, audio_file.read())}
                response = requests.post(url, headers=headers, files=files, data=data)
                response_json = response.json()
                transcript = response_json.get('transcription', '')
                transcript = transcript.replace('\n', ' ')
                therapy_report = therapy_report_fn(transcript)
                therapy_session = therapy_session_fn(transcript)
                comprehension_report = compre_fn(transcript)
                next_session_blueprint = blueprint_fn(transcript)
                goal= goal_fn(transcript)
                feedback =feedback_fn(transcript)
                meeting_transcript = MeetingTranscript.objects.create(
                    user=request.user,
                    therapy_report=therapy_report['outputs'][0]['text'],
                    therapy_session=therapy_session['outputs'][0]['text'],
                    comprehension_report=comprehension_report['outputs'][0]['text'],
                    next_session_blueprint=next_session_blueprint['outputs'][0]['text'],
                    goal= goal['outputs'][0]['text'],
                    feedback=feedback['outputs'][0]['text']
                )
                meeting_transcript.save()
                return JsonResponse({'success': 'Audio file transcribed and stored successfully.'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'An error occurred while processing the audio file.'}, status=500)
    else:
        form = AudioUploadForm()
    return render(request, 'transcribe.html', {'form': form})


# views.py
from django.shortcuts import render
from .models import MeetingTranscript

def view_transcripts(request):
    transcripts = MeetingTranscript.objects.filter(user=request.user)
    return render(request, 'view_transcripts.html', {'transcripts': transcripts})

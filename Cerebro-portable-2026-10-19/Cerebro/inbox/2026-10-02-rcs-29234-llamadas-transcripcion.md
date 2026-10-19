# RCS-29234 ADUSA, llamadas del 2 oct 2026. Transcripcion

Fuente: audios "Carrera 73 24" (10 min, interna) y "Carrera 73 25" (8 min, con el cliente), en ingles. Whisper medium local.
Nombres corregidos a mano: Karen es Kiran, One y Vaughn son Juan, "I hold their heads" es Ahold Delhaize, "medical 901" es Medical911.
Sin resolver: "review the Lawson" en 00:27 y "test Gina" en 02:05. Hablantes no separados por el modelo.

## Llamada 1, interna. J.R., Kiran, Juan, Sebastian Garces

[00:10] Hi, you're
[00:21] Okay, I think we I think we need to recreate
[00:27] Similar incident for for review the Lawson
[00:31] Okay, but we need like a test place to do this because we don't want to do it to a customer environment
[00:37] Because if I recall what we did last night
[00:41] Yeah, so, you know the app will go down for everybody for a little bit if we do that if I'm remembering that, right?
[00:48] So I'm gonna be careful
[00:50] Okay. Okay. I'm also open to not work on this all weekend
[00:54] so
[00:56] Let's see what we can do. Hey Kiran
[00:58] Hi, guys
[01:01] Hi
[01:12] I do
[01:15] Analysis, but I think we can easily recreate it
[01:18] But if you want trying to fix it from the core perspective because I'm only concerned in that part
[01:24] I can think you know, we need to do you know check the core and stuff
[01:29] But if you're thinking oh, this is web server cache
[01:32] So that involves in part time if you're thinking of a root cause if and if it's purely on them
[01:38] Then I am not good at
[01:41] Suggesting what should be
[01:43] Thinking it's the code one. Yeah, then then even then it's a long shot like like we have to test it get the test
[01:52] Oh, you know recreate the scenario. Oh, we find the issue now that there is code involved and we
[01:58] Tested and changing of codes and we because this universal for all the platform question clients
[02:03] This has to be better through
[02:05] Properly through right channels. We push it to test Gina and the QA team
[02:10] We'll rip it apart try and make this and I remember this issue being fixed
[02:15] This is long ago even before platform question came in and you know initial baby steps. We figured this out
[02:21] I'm not trying to
[02:23] You know the work on somebody else
[02:26] But I think it is also good angle to see if infra has anything going and also this is purely ADUSA, so like
[02:33] Ahold Delhaize is coming forward and saying this which makes me believe this is not a code issue
[02:38] It is something with them but again how many people do actually regularly change
[02:43] forms that they have that might also be the reason that's why nobody's complaining because users once they set their forms
[02:48] They are not playing with them. I guess so
[02:52] Not entirely sure. So yeah, so I'm like debating is that on on infra or is that on code? I'm still no
[03:00] Still not sure entirely. So here's my thoughts
[03:03] I worry that
[03:05] You know if they make any of the well first I want to understand
[03:09] If at all possible and I recognize it might not be because again if we had that date change field
[03:16] I think we could hone in on this easier. I would love to understand. Did they make the change that caused this?
[03:22] even defective manifest right like
[03:25] Even if it's a defect or not
[03:27] Like did they do something that made it happen because if we can find what that is we can say stop doing that
[03:34] until
[03:36] Exactly. Yes, that that would be my solution at the moment in this Friday evening
[03:41] If you want we can redo do exactly the same thing and then those guys can you please hold up to a Monday making
[03:46] Any changes and carry about your work during this weekend and and that's ideal
[03:51] The problem will be if we can't figure out that that is the cause and we tell them this and
[03:58] Then they don't make any changes and then they run into the same problem
[04:02] But to your point
[04:04] I'm a person that runs by statistics and odds, right?
[04:08] Statistically, nobody else knock on wood is complaining about this. It's just all exactly and we know he's making changes to case type
[04:15] So it's probably that so what I'd love to do is get on a call with Jim say hey Jim
[04:19] Were you guys making changes to case types? I know you said that Leigh Ann was gonna do that today
[04:23] If so, cool. Stop that while we're gonna look into it early next week. We're gonna
[04:29] We're gonna rebuild all your screens again, which hopefully you're on and Sebastian can now do the thing
[04:34] They were trying to do last night and couldn't do I don't want you to do it here
[04:37] And I want us to do it so that we can make sure it works for us
[04:40] So let's rebuild all the screens and then don't do this yet. This is just a plan
[04:45] I'm talking about then we'll bounce the app which I think bounces the app for everybody for a few minutes
[04:50] Is that right? Yes
[04:53] Okay, so should we send a notification out to all customers that the app might run slow for five minutes
[04:58] so should we just roll the dice on a Friday and
[05:02] That that nobody's gonna notice or call us up to you
[05:05] J.R., like sending out communication is not isn't gonna hurt if it's only safer to do it. Yeah, normally I would
[05:13] But again, it's Friday evening. Do you think it's highly head if you have the numbers you see if it not the case as usual
[05:20] If it's any lesser then we can probably
[05:24] Normally I would
[05:30] Status page I would just put a note on the status page and say hey, you know, we're rebooting the service
[05:35] It's gonna be down for five minutes. We don't have a status page
[05:37] So we have we do have the ability within the app to send a notification
[05:42] But sending a notification in the app that's gonna be down is not you know, that's not exactly an album here
[05:49] So I I'm almost inclined I
[05:52] Don't like saying this I'm almost inclined to roll the dice just because getting a customer communication email out is gonna take
[05:58] So long at this point. Yeah, it's probably gonna be five minutes. I agree
[06:11] So now rereading what Jim said we know he made the change he went into screen designer went to Medical 911
[06:17] And he says he knows they clicked save and build
[06:21] which I
[06:23] Won't be surprised. You know what I mean? They I go back to my earlier statement of from yesterday
[06:28] This happening across all their different case types at the same time leads me to believe that something he did trigger to defect on our side
[06:37] So I think Matt's back Monday so we can dive deeper into that Monday and exactly the steps we want to recreate it
[06:44] We'll bounce back and you know, they'll restart the app servers again if need be but let him show us step-by-step
[06:50] I'm gonna capture it on you know, let's record it and see what exactly is he doing and
[06:55] I'm thinking it's pretty easy
[06:58] Because you know you just make the field delete a field add a field like delete the same field and add the same field
[07:03] Or delete that field and add something else just so that we have more clarity
[07:06] Which one is coming up and then they'll save and build and use it
[07:11] I think it's gonna give us the old one, which is that you just deleted and it's gonna say
[07:15] Oh, I don't belong here because I'm not on the file, but it actually belongs to the table
[07:19] I think it's pretty easy just to come home. We can only do that on either
[07:25] We can only do that on a test environment, right because yeah
[07:28] I mean if Jim has something to show us and he can do awesome on part, but if we are playing
[07:35] Absolutely on test we can do it on test
[07:37] Yeah
[07:38] We have to do it on test because if we do it on we're gonna have to bounce the app twice and there's no
[07:43] Way of bouncing the app twice just to test something in the middle of the day. Okay, so
[07:47] That's let's see if okay. So here's the plan
[07:51] Juan, I need you to work with Sebastian
[07:54] Get a test environment going after we talk to Jim and then try to recreate this on your own for Jim
[08:00] I'm gonna get him on a call. I'm gonna tell him stop for today through the weekend
[08:05] Stop until we come back to you hitting save or save and build we need to investigate this and that's back Monday
[08:11] So we're gonna get on it Monday
[08:12] I'm gonna tell him we're gonna do a little bit of testing on our side and then we're gonna do the exact
[08:17] Same thing we did last time and once we do that, then it will let him know so that he's good to go at that point
[08:22] Okay. Yes, okay
[08:26] That's all right Kiran, I'm just I'm trying to deep risk ourselves because what I don't want is this all to be on another
[08:33] That's the right thing to do yeah, like
[08:36] Whatever is, you know easiest and best and efficient for all of us not just them and us, you know
[08:43] We'll take that route
[08:45] Excellent
[08:48] I am peeling up at the moment guys
[08:50] So that's where I'm like going a little slow so that I can and if you guys have anything else
[08:55] Please go ahead cry it and let me know if you have questions with regards to how to recreate the scenario
[09:00] I'm gonna pop over
[09:02] Into the and Sebastian, Juan, I would like you to do the same thing into the call from last night that we had with
[09:08] Jim I'm just gonna use the exact same one. I'm gonna connect into that meeting and
[09:12] We'll wait we'll talk to Jim and then we'll go do our testing and Kiran will let you know what we found out
[09:16] We'll record that call
[09:20] Are we gonna
[09:22] Once the server right now or later? Not yet. Not yet. Let us talk to Jim first then let us reproduce the scenario
[09:29] Then we'll okay. You guys let me know when it's a green signal and we'll jump on a call and do it together
[09:34] Sounds great. Sounds great. And guys while we're doing this. Thanks Kiran. Juan and Sebastian
[09:40] Find those instructions that Kiran sent us on how to rebuild all screens at once get ready for that
[09:45] Don't rebuild them yet, but get ready for that. Okay, okay
[09:47] actually
[09:48] You can even rebuild them who gives a shit because the it's not gonna impact his
[09:52] Service and we have to bounce the server before it takes effect
[09:54] So try that all screen rebuild because if we need her to do it then we'll have to let her know
[09:59] Okay, so let's hop over to the other channel. I'm gonna ping it so you guys can see it
[10:04] Okay. Yeah, Jim. Thanks guys

## Llamada 2, con ADUSA. J.R., Jim Cosseboom, Leigh Ann Stubbs, Juan, Sebastian

[00:02] That might have been some of the source of the issue, but today
[00:06] again, it's two
[00:08] Two case entry screens which are used for most of these one is central station master, which does most of them
[00:16] That was not touched today
[00:19] That seemed to be working just fine
[00:21] The Medical 911 is the other page which is used for our medical
[00:27] We went we added
[00:29] Leigh Ann added a couple fields into it said save and build
[00:35] And again typically looking at the screen then refresh your case and see okay
[00:40] Are they showing up but sometimes you do have to go into hide display fields and unhide it if it's still hidden
[00:47] It worked that way built built it
[00:53] Case
[00:54] Entered the data in the first time. It's a
[00:58] And we're right back to the screen and all the data that had been entered
[01:02] Next time we went we could say we just hit the spinning processing and it's
[01:11] So almost behaving this and looked and it's yet still spinning in process in the test case I put in
[01:18] So I think two is it number one. I'm like to see if we can do so I do the fix
[01:24] We did last night get us back to baseline, but I think longer term
[01:30] It is a clearly seems to be a bug with the save and build
[01:35] Obviously, we will not be doing any saving and building until we address that but that's not something that needs to be addressed
[01:40] That was gonna be my very first ask was let's pause, you know until we get this identified
[01:49] So just to be clear though, it's only happening in the Medical 911 ones. You can actually save them in other case types
[01:56] It's the it's the case
[02:00] Cases that use the Medical 911
[02:03] Screen, which I think is just probably the medical case type
[02:07] But you can do other case types and save them without issue
[02:11] Correct they use other yes, like though I the critical instance that use the page type central station master
[02:17] I tested one of those and it went it behaved just fine
[02:23] That's good information for engineering because yesterday you were only working on the other case type and it seemed to make every case type
[02:30] Have that issue?
[02:31] Well, it was a case and it was a case entry screen as opposed to case type
[02:36] Case entry screen central station master you use by a lot of case types. Okay. Okay, so that's why that case
[02:45] Okay
[03:05] I
[03:13] Mean get the expert to come in and do it. So all good. The reason I ask is in our database
[03:20] We actually have a field that shows when you click save versus when you hit save and build but because
[03:25] We unmarried that from the GUI. It hasn't been updated in two or three years
[03:29] So I could easily go in if that field was working in the back end in the database and see what you clicked
[03:35] But I can't all I can see is when you click save and build
[03:39] So I have to ask the question today. I have a defect filed for that or one should have filed a defect for that
[03:43] This morning, so we'll get that resolved for troubleshooting cool. So here's the plan
[03:48] right now Juan and team are going to
[03:51] Try to reproduce this elsewhere, but simultaneously we're rebuilding your screens right now
[03:58] And if you recall rebuilding your screens is gonna run into that caching issue somewhere in our pipeline
[04:04] So we're going to do something that I don't do during the day normally and that is we're going to bounce the app
[04:11] Just like we did last night. So it'll go down for three to five minutes
[04:14] You know in the middle of the day, so we're gonna rebuild your screens. Once all the rebuilds are done
[04:18] We'll work with engineering. We'll bounce the app
[04:21] And then we'll let you know via the ticket
[04:24] Simultaneously, we're gonna work in a test environment and we're gonna try to reproduce
[04:29] Exactly what you did so Leigh Ann if you could do me a favor I have this recording and I very much appreciate that
[04:36] If you could just write down your steps as well in the email and send them back to me
[04:41] I see you're on the email that way. I can also send that to engineering
[04:44] I'll send them this recording the transcription and your documented versions of the steps you took that caused this issue
[04:50] So that way we can try to get to root cause. Yep. Are you good with that Leigh Ann?
[04:54] Perfect Matt's back Monday and candidly that you know, Matt Kamminga and I know you know Matt
[05:01] We've worked with him on a lot of different issues. He's the one that basically runs this product from an engineering perspective
[05:06] He was he took a two-week vacation. He's like never again that can't can't take vacation. Sorry, buddy
[05:17] I tried to take short vacations too for exactly that reason. It's like a Friday and a Monday
[05:24] Everything of course
[05:27] So awesome. All right, if we're gonna if we're good to do that
[05:31] sort of do the fix we did last time for the short term and we won't touch any case building and we'll investigate further and
[05:38] see what the glitch is and
[05:43] That's something
[05:45] Next week normal. That's not a critical
[05:47] Critical issue. These are nice. These are things we want to do that you develop. It's not something we need to do
[05:54] Yeah, no, I get you 100% and but to be fair if Matt was here
[05:57] I would be asking that to work on this today because while it's easy for me to say to you
[06:02] Hey Jim and Leigh Ann, please don't do this over the weekend
[06:04] We got hundreds of other customers and I've run the risk with every single one of them that they're gonna try this
[06:10] Today now the good news is a lot of customers set this up in the beginning and then don't really ever touch it again
[06:15] You guys are a lot more mature than a lot of our other customers when it comes to using these so
[06:20] I'm just crossing my fingers. We'll see how it goes over the weekend. All right, Jim. I'll be back with you soon Leigh Ann
[06:25] I'll keep an eye out for your email and
[06:27] Juan and Sebastian if you could hang on so we can just make sure we're crisp on next steps. I appreciate it. Thanks
[06:36] All right, so
[06:39] Just to be clear
[06:41] Rebuild the screens right now and as soon as the rebuild it lets in the chat
[06:46] Tell Kiran that the rebuild is happening and then we'll tell Kiran when the all the rebuilds are done
[06:52] I'll get her this recording of this
[06:55] Then we'll work with her to bounce the app
[07:00] Simultaneously whoever's not rebuilding the screens out of you too
[07:02] And if you guys want to do it together to get it working, that's okay
[07:05] But I need somebody to then go into a test environment
[07:07] Once we get Leigh Ann's instructions and try to do as close to what she's doing as we can
[07:13] To see if we can get the same thing to happen because it's still possible
[07:16] They have something configured on their side that makes it where they're the only ones that are gonna run into this defect
[07:21] So let's just try to get as much information for engineering as we can here, please
[07:29] Gentlemen, thank you very much. I appreciate it. I appreciate you quickly leaving on this one again. Thank you
[07:36] Thank you

function selectTenses(responses) {
    var indicative = responses.substring(0,5);
    var subjunctive = responses.substring(5,9);
    var imperative = responses.substring(9,11);
    var progressive = responses.substring(11,16);
    var perfect = responses.substring(16,21);
    var subPerfect = responses.substring(21,24);

    var selected = [indicative, subjunctive,
		    imperative, progressive,
		    perfect, subPerfect]
    
    var voiceMoods = ["Indicative", "Subjunctive", "Imperative",
		      "ContinuousProgressive", "Perfect",
		      "PerfectSubjunctive"]
    var indicativeTenses = ["Present", "Preterite", "Imperfect",
			    "Conditional", "Future"]
    var subjunctiveTenses = ["Present", "Imperfect",
			     "Imperfect2", "Future"]
    var imperativeTenses = ["Affirmative", "Negative"]
    var progressiveTenses = ["Present", "Preterite", "Imperfect",
			     "Conditional", "Future"]
    var perfectTenses = ["Present", "Preterite", "Past",
			 "Conditional", "Future"]
    var subPerfectTenses = ["Present", "Past", "Future"]

    var allTenses = [indicativeTenses, subjunctiveTenses,
		     imperativeTenses, progressiveTenses,
		     perfectTenses, subPerfectTenses]
    
    var chosenIndicative = []
    var chosenSubjunctive = []
    var chosenImperative = []
    var chosenProgressive = []
    var chosenPerfect = []
    var chosenSubPerfect = []
    chosen = [chosenIndicative, chosenSubjunctive,
	      chosenImperative, chosenProgressive,
	      chosenPerfect, chosenSubPerfect]
    var chosenMoods = []
    for (var moodChoiceIndex = 0;
	 moodChoiceIndex < allTenses.length; moodChoiceIndex++)
    {
	
	for (var tenseChoiceIndex = 0;
	     tenseChoiceIndex < allTenses[moodChoiceIndex].length;
	     tenseChoiceIndex++)
	{
	    if (selected[moodChoiceIndex].charAt(tenseChoiceIndex) === "1") {
		chosen[moodChoiceIndex].push(
		    allTenses[moodChoiceIndex][tenseChoiceIndex])
	    }
	}
	if (chosen[moodChoiceIndex].length > 0) {
	    chosenMoods.push(voiceMoods[moodChoiceIndex])
	}
	
    }

    var fakeVerbObj = {
	Indicative: chosenIndicative,
	Subjunctive: chosenSubjunctive,
	Imperative: chosenImperative,
	ContinuousProgressive: chosenProgressive,
	Perfect: chosenPerfect,
	PerfectSubjunctive: chosenSubPerfect
    }
    return [fakeVerbObj, chosenMoods]
}

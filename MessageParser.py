import json

class MessageParser():
    def __init__(self):
        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history
            
	    # More key:values pairs are needed	
        }
    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            return 'unvalid'

    def parse_error(self, payload):
        errorDict = json.loads(payload)
        errorString = errorDict['content']
        return errorString
    
    def parse_info(self, payload):
        infoDict = json.loads(payload)
        infoString = infoDict['content']
        return infoString

    def parse_message(self, payload):
        messageDict = json.loads(payload)
        messageString = messageDict['content']
        return messageString

    def parse_history(self, payload):
        historyDict = json.loads(payload)
        historyString = historyDict['content']
        return historyString

import requests
import string

def test_blacklisted_chars():
    url = "http://shape-facility.picoctf.net:59297/announce"
    
    # Characters to test (including special chars commonly blacklisted)
    test_chars = '_{}[]|$@.\\/<>?;:\'"!~`%^&*()+-='
    
    blacklisted = []
    
    for char in test_chars:
        # Test with a simple payload containing the character
        payload = f"{{{{ '{char}' }}}}"
        
        try:
            response = requests.post(url, data={'content': payload}, timeout=5)
            
            # Check for the specific error message
            if "Stop trying to break me" in response.text:
                print(f"Character '{char}' appears to be blacklisted (triggered error message)")
                blacklisted.append(char)
            else:
                print(f"Character '{char}' seems allowed")
                
        except Exception as e:
            print(f"Error testing character '{char}': {e}")
            blacklisted.append(char)
    
    print("\nBlacklisted characters:")
    print(blacklisted)
    return blacklisted

if __name__ == "__main__":
    test_blacklisted_chars()

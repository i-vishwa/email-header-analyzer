import gradio as gr
import re
from email import message_from_string

def extract_email_info(raw_headers):
    try:
        # Parse headers using the email module
        msg = message_from_string(raw_headers)
        results = {}

        # Get basic fields
        results["From"] = msg.get("From", "Not Found")
        results["To"] = msg.get("To", "Not Found")
        results["Subject"] = msg.get("Subject", "Not Found")
        results["Return-Path"] = msg.get("Return-Path", "Not Found")

        # Extract all IPs from 'Received' headers
        received_headers = msg.get_all("Received", [])
        ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
        ip_list = []

        for header in received_headers:
            found_ips = re.findall(ip_pattern, header)
            ip_list.extend(found_ips)

        results["Relay IPs (from Received headers)"] = list(set(ip_list)) if ip_list else "No IPs found"

        # Basic spoofing detection: compare Return-Path and From
        if results["Return-Path"] != "Not Found" and results["From"] != "Not Found":
            if results["Return-Path"] != results["From"]:
                results["Spoofing Suspicion"] = "⚠️ Possible spoofing detected"
            else:
                results["Spoofing Suspicion"] = "✅ No spoofing detected"
        else:
            results["Spoofing Suspicion"] = "⚠️ Insufficient data to verify spoofing"

        # Format output
        output_text = "\n".join(f"{key}: {value}" for key, value in results.items())
        return output_text

    except Exception as e:
        return f"Error processing headers: {str(e)}"

# Gradio Interface
iface = gr.Interface(
    fn=extract_email_info,
    inputs=gr.Textbox(lines=15, placeholder="Paste raw email headers here..."),
    outputs="text",
    title="Email Header Analyzer",
    description="Paste raw email headers to extract sender details, IP addresses, and check for spoofing."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=8080)




import argparse
from modules.vulnerability_scanner import VulnerabilityScanner
from modules.ai_validator import AdvancedAIValidator
from modules.pdf_report import PDFReport
from modules.subdomain_enum import SubdomainEnumerator

def main():
    parser = argparse.ArgumentParser(description="Advanced Vulnerability Assessment Tool")
    parser.add_argument('--url', type=str, required=True, help='Target URL')
    parser.add_argument('--output', type=str, required=True, help='Output PDF report file name')
    args = parser.parse_args()

    url = args.url
    output = args.output

    print(f"[*] Enumerating subdomains for {url}")
    subdomains = SubdomainEnumerator().enumerate(url)
    
    print(f"[*] Scanning for vulnerabilities on {url}")
    scanner = VulnerabilityScanner()
    vulnerabilities = scanner.scan(url, subdomains)
    
    print("[*] Validating vulnerabilities using AI module")
    validated_vulns = AdvancedAIValidator().validate(vulnerabilities)
    
    print(f"[*] Generating PDF report: {output}")
    PDFReport().generate(validated_vulns, output)
    
    print("[*] Assessment Complete!")

if __name__ == "__main__":
    main()

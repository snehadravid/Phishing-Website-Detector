
from urllib.parse import urlparse
import re
import ipaddress


def extract_features(url):
    # Add scheme if missing
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed_url = urlparse(url)
    domain = parsed_url.hostname or ""

    # Check whether the domain is an IP address
    try:
        ipaddress.ip_address(domain)
        is_ip = 1
    except ValueError:
        is_ip = 0

    # Count subdomains
    domain_parts = domain.split(".") if domain else []
    subdomains = max(0, len(domain_parts) - 2)

    features = {
        "URLLength": len(url),
        "DomainLength": len(domain),
        "IsDomainIP": is_ip,
        "NoOfSubDomain": subdomains,
        "IsHTTPS": 1 if parsed_url.scheme == "https" else 0,
        "NoOfLettersInURL": sum(c.isalpha() for c in url),
        "NoOfDegitsInURL": sum(c.isdigit() for c in url),
        "NoOfEqualsInURL": url.count("="),
        "NoOfQMarkInURL": url.count("?"),
        "NoOfAmpersandInURL": url.count("&"),
        "NoOfOtherSpecialCharsInURL": sum(
            not c.isalnum() for c in url
        ),
    }

    return features

import argparse
import json
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Creates JSon to power verified builds html""")
    parser.add_argument('--merge-time', type=str, help='merge-time')
    parser.add_argument('--branch', type=str, help='branch')
    parser.add_argument('--git-short-sha', type=str, help='git commit ')
    parser.add_argument('--full-checksum', type=str, help='checksum')
    parser.add_argument('--pr-number', type=str, help='pr-number')
    parser.add_argument('--title', type=str, help='title')
    parser.add_argument('--release-notes', type=str, help='title')
    parser.add_argument('--download-url', type=str, help='download url')
    parser.add_argument('--deb-file-name', type=str, help='deb file name')
    parser.add_argument('--file', type=str, help='file to write into')

    args = parser.parse_args()

    # Get the first 5 characters
    sum_first_5 = args.full_checksum[:5]
    # Get the last 5 characters
    sum_last_5 = args.full_checksum[-5:]
    abbr_checksum = sum_first_5 + "..." + sum_last_5
    # init data structure
    data = []

    if ! args.release_notes:
        record = {
            "merge-time": args.merge_time,
            "branch": args.branch,
            "git-short-sha": args.git_short_sha,
            "full-checksum": args.full_checksum,
            "abbr-checksum": abbr_checksum,
            "pr-number": args.pr_number,
            "title": args.title,
            "download-url": args.download_url,
            "deb-file-name": args.deb_file_name,
        }
    else
        record = {
            "merge-time": args.merge_time,
            "branch": args.branch,
            "git-short-sha": args.git_short_sha,
            "full-checksum": args.full_checksum,
            "abbr-checksum": abbr_checksum,
            "pr-number": args.pr_number,
            "title": args.title,
            "release-notes": args.release_notes,
            "download-url": args.download_url,
            "deb-file-name": args.deb_file_name,
        }

    if os.path.exists(args.file):
        with open(args.file, 'r') as build_history_json:
            if build_history_json:
                data = json.load(build_history_json)

    data.append(record)

    with open(args.file, 'w') as file:
        json.dump(data, file, indent=4)

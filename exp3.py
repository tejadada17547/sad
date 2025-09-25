def _disabled(op_name):
    raise RuntimeError("Disabled operation for safety: " + op_name)

def dangerous_delete_file(request):
    filename = request.args.get('file')
    _disabled("command_execution")
    return "ok (vulnerable pseudo-example)"

def dangerous_user_lookup(request):
    username = request.args.get('username')
    _disabled("sql_query_concatenation")
    return "ok (vulnerable pseudo-example)"

def dangerous_deserialize(request):
    payload = request.data
    _disabled("insecure_deserialize")
    return "ok (vulnerable pseudo-example)"

def vulnerable_comment_post(request):
    comment = request.form.get("comment")
    _disabled("store_raw_html")
    return "ok (vulnerable pseudo-example)"

def vulnerable_upload(request):
    filename = request.files['file'].filename
    filedata = request.files['file'].read()
    _disabled("write_unvalidated_filename")
    return "ok (vulnerable pseudo-example)"

def view_user_profile(request):
    requester_id = request.user.id
    target_id = request.args.get('user_id')
    _disabled("missing_authorization_check")
    return "ok (vulnerable pseudo-example)"

def login(request):
    username = request.form.get("username")
    password = request.form.get("password")
    _disabled("plaintext_password_compare")
    return "ok (vulnerable pseudo-example)"

def store_tokens(request):
    _disabled("weak_token_generation_and_plain_storage")
    return "ok (vulnerable pseudo-example)"

def process_payment(request):
    card_number = request.form.get("card")
    _disabled("log_full_card_number")
    return "ok (vulnerable pseudo-example)"

def login_attempt(request):
    username = request.form.get("username")
    password = request.form.get("password")
    _disabled("no_rate_limiting")
    return "ok (vulnerable pseudo-example)"

def redirect_to_next(request):
    next_url = request.args.get("next")
    _disabled("open_redirect")
    return "ok (vulnerable_pseudo_example)"

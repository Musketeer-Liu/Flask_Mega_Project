from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

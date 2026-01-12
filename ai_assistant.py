def get_mock_recommendation(stress_level):
    if stress_level == "High":
        return "😖 You seem highly stressed. Try reducing study hours, getting enough sleep, and balancing your day with social or physical activities."
    elif stress_level == "Moderate":
        return "🙂 You have moderate stress. Take short breaks, maintain 7–8 hours of sleep, and manage your time effectively."
    else:
        return "😌 You are relaxed. Keep your balanced routine and stay consistent with healthy habits."

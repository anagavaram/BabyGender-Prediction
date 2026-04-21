import numpy as np
import pandas as pd
import joblib

NAME_FEATURES = ['name_len', 'last_letter_enc', 'last_2_enc',
                 'first_letter_enc', 'vowel_count', 'ends_in_vowel']
GROWTH_FEATURES = ['age_months', 'weight_kg', 'height_cm', 'bmi', 'weight_per_cm']

class BabyGenderEnsemble:
    def __init__(self):
        self.name_model = joblib.load('models/name_gender_model.pkl')
        self.growth_model = joblib.load('models/growth_gender_model.pkl')
        self.encoders = joblib.load('models/name_encoders.pkl')
        self.scaler = joblib.load('models/growth_scaler.pkl')

    def predict_from_name(self, name):
        name = name.strip().capitalize()
        le = self.encoders
        feats = pd.DataFrame([[
            len(name),
            self._safe_encode(le['le_last'], name[-1].lower()),
            self._safe_encode(le['le_last2'], name[-2:].lower()),
            self._safe_encode(le['le_first'], name[0].lower()),
            sum(1 for c in name.lower() if c in 'aeiou'),
            int(name[-1].lower() in 'aeiou')
        ]], columns=NAME_FEATURES)
        prob = self.name_model.predict_proba(feats)[0]
        return {'Female': round(prob[0], 3), 'Male': round(prob[1], 3)}

    def predict_from_growth(self, age_months, weight_kg, height_cm):
        bmi = weight_kg / (height_cm / 100) ** 2
        wpc = weight_kg / height_cm
        raw = pd.DataFrame([[age_months, weight_kg, height_cm, bmi, wpc]],
                           columns=GROWTH_FEATURES)
        scaled = pd.DataFrame(self.scaler.transform(raw), columns=GROWTH_FEATURES)
        prob = self.growth_model.predict_proba(scaled)[0]
        return {'Female': round(prob[0], 3), 'Male': round(prob[1], 3)}

    def _safe_encode(self, le, val):
        if val in le.classes_:
            return le.transform([val])[0]
        return 0

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Baby Gender Predictor')
    parser.add_argument('--name', type=str, help='Baby name to predict gender')
    parser.add_argument('--age', type=float, help='Age in months')
    parser.add_argument('--weight', type=float, help='Weight in kg')
    parser.add_argument('--height', type=float, help='Height in cm')
    args = parser.parse_args()

    ensemble = BabyGenderEnsemble()

    if args.name:
        result = ensemble.predict_from_name(args.name)
        print(f'Name: {args.name} -> {result}')

    if args.age is not None and args.weight is not None and args.height is not None:
        result = ensemble.predict_from_growth(args.age, args.weight, args.height)
        print(f'Growth ({args.age}mo, {args.weight}kg, {args.height}cm) -> {result}')

    if not args.name and (args.age is None or args.weight is None or args.height is None):
        parser.print_help()


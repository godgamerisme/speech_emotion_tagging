export type Patient = {
  name: String;
  gender: String;
  age: Number;
};

export type Session = {
  patient: Patient
  doctor: String;
  date: Date;
}

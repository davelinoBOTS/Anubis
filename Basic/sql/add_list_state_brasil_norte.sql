INSERT INTO public."Basic_state"(
	id, "registrationDate", "updateDate", "codeIBGE", name, acronym, "isActive", country_id)
	VALUES 
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '11', 'Rondônia', 'RO', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '12', 'Acre', 'AC', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '13', 'Amazonas', 'AM', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '14', 'Roraima', 'RR', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '15', 'Pará', 'PA', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '16', 'Amapá', 'AP', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '17', 'Tocantins', 'TO', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA'));
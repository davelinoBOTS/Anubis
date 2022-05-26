INSERT INTO public."Basic_state"(
	id, "registrationDate", "updateDate", "codeIBGE", name, acronym, "isActive", country_id)
	VALUES 	
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '31', 'Minas Gerais', 'MG', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '32', 'Espírito Santo', 'ES', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '33', 'Rio de Janeiro', 'RJ', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '35', 'São Paulo', 'SP', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA'));
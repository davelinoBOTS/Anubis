INSERT INTO public."Basic_state"(
	id, "registrationDate", "updateDate", "codeIBGE", name, acronym, "isActive", country_id)
	VALUES 
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '41', 'Paraná', 'PR', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '42', 'Santa Catarina', 'SC', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '43', 'Rio Grande do Sul', 'RS', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA'));
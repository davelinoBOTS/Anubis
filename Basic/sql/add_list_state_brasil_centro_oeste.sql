INSERT INTO public."Basic_state"(
	id, "registrationDate", "updateDate", "codeIBGE", name, acronym, "isActive", country_id)
	VALUES
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '50', 'Mato Grosso do Sul', 'MS', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '51', 'Mato Grosso', 'MT', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '52', 'Goiás', 'GO', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '53', 'Distrito Federal', 'DF', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA'));
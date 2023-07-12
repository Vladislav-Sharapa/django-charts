CREATE TABLE MessageLog(
    ID serial PRIMARY KEY,
    YEARREG                   INT           not null,
    STATE                     VARCHAR(5)    not null,
    DATE_RCV                  DATE          not null,
    TYPE_DOC                  VARCHAR(7)    not null,
    CUSTOM                    VARCHAR(2),
    PTO                       VARCHAR(3),
    DECLARANT_UNP             VARCHAR(20),
    FULLNAME                  VARCHAR(150),
    STATUS                    VARCHAR(2),
    STATUS_DOC                VARCHAR(2)
);



INSERT INTO MessageLog(
    YEARREG, STATE, DATE_RCV,
    TYPE_DOC,  CUSTOM, PTO,
    DECLARANT_UNP, FULLNAME, STATUS, STATUS_DOC
)
VALUES
    ('2023', '3', '2023-07-03', 'SD', '01', '111', 'Exporter', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2022', '2', '2023-07-06', 'DT', '01', '111', 'Importer', 'Ivanov Ivan Ivanovich', '01', '06'),
    ('2022', '3', '2023-07-06', 'PT', '01', '222', 'Consignee', 'Pronevich Ivan Ivanovich', '01', '04'),
    ('2023', '1', '2023-07-08', 'SD', '01', '333', 'Сonsignor', 'Milkevich Ivan Ivanovich', '03', '04'),
    ('2023', '3', '2023-07-04', 'NF', '01', '222', 'Exporter', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2023', '3', '2023-07-03', 'PT', '01', '111', 'Importer', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2023', '2', '2023-07-03', 'SD', '01', '444', 'Consignee', 'Ivanov Ivan Ivanovich', '00', '01'),
    ('2023', '1', '2023-07-06', 'TF', '01', '231', 'Exporter', 'Ivanov Ivan Ivanovich', '00', '02'),
    ('2023', '2', '2023-07-11', 'SD', '01', '111', 'Сonsignor', 'Ivanov Ivan Ivanovich', '04', '01'),
    ('2023', '3', '2023-07-14', 'PT', '01', '123', 'Exporter', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2023', '1', '2023-07-12', 'PT', '01', '111', 'Importer', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2023', '2', '2023-07-15', 'PT', '01', '232', 'Exporter', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2023', '3', '2023-07-13', 'PT', '01', '222', 'Exporter', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2023', '2', '2023-07-15', 'TF', '01', '222', 'Exporter', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2023', '1', '2023-07-11', 'SD', '01', '333', 'Exporter', 'Ivanov Ivan Ivanovich', '00', '04'),
    ('2023', '2', '2023-07-15', 'SD', '01', '444', 'Importer', 'Ivanov Ivan Ivanovich', '00', '04')